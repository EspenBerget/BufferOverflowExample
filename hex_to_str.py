# “hex_to_str.py”
import sys
import re

def hex_to_str(hex_str):
    matches = re.findall(r"[0-9a-f]{2}", hex_str)
    return "".join(map(lambda x: chr(int(x, 16)), matches))


for line in map(str.rstrip, sys.stdin):
    print(hex_to_str(line))



