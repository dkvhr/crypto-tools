from Crypto.Util.number import bytes_to_long, long_to_bytes

def broadcast_attack(ns, cs, e):
    c = int(pow(crt(cs, ns), 1/e))
    return long_to_bytes(c)
