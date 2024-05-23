from Crypto.Util.number import bytes_to_long, long_to_bytes
from decimal import Decimal, getcontext

getcontext().prec=1000

def broadcast_attack(ns, cs, e):
    m = int(pow(crt(cs, ns), 1/e))
    return long_to_bytes(m)


#This will only work if m**e < N
def small_e(c, e):
    m = int(Decimal(c) ** (Decimal(1) / Decimal(3))) + 1
    return m

