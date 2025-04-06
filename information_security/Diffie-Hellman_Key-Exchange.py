import time
import random
import hashlib

g = 2
p = "009fdb8b8a004544f0045f1737d0ba2e0b274cdf1a9f588218fb435316a16e374171fd19d8d8f37c39bf863fd60e3e300680a3030c6e4c3757d08f70e6aa871033"

def mod_exp(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % g == 1:
            result = (result * base) % mod
        base = (base ** g) % mod
        exponent =exponent / g
    return result

def diffie_hellman_key(private_key, public_value, prime):
    return mod_exp(public_value, private_key, prime)

a1 = input("a : ")
b1 = input("b : ")

a = int(a1, 16)
b = int(b1, 16)

t1 = time.time()
A = mod_exp(g, a, int(p, 16))
time_A = (time.time() - t1) * 1000

t2 = time.time()
B = mod_exp(g, b, int(p, 16))
time_B = (time.time() - t2) * 1000

t3 = time.time()
KA = diffie_hellman_key(b, A, int(p, 16))
time_KA = (time.time() - t3) * 1000

t4 = time.time()
KB = diffie_hellman_key(a, B, int(p, 16))
time_KB = (time.time() - t4) * 1000

print(f"A = {hex(A)}, 𝑇𝐴 = {time_A:.2f} ms")
print(f"B = {hex(B)}, 𝑇𝐵 = {time_B:.2f} ms")
print(f"𝐾𝐴 = {hex(KA)} 𝑇𝑘𝐴 = {time_KA:.2f} ms")
print(f"𝐾𝐵 = {hex(KB)} 𝑇𝑘𝐵 = {time_KB:.2f} ms")
