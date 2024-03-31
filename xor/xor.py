import binascii
from Crypto.Util.number import long_to_bytes

def xor_bytes(a, b, base):
    # receives two byte streams and returns their xor
    return int(a, base) ^ int(b, base)

def xor(a, b):
    # simple xor
    return a ^ b

def xor_bruteforce_key(m, max_tries):
    for i in range(1, max_tries):
        print(long_to_bytes(m ^ i))
    return

