We were given n which is a prime(instead it should be p*q in RSA).So here to find d we just need to find modinv of e and n-1(in usual RSA it would be e and (p-1)*(q-1)) 

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEBITsFfW/evEUntbdCGsHp
PM/+p2xPCHSZHPP6zw6rnvZGohg5ggtNZTqRa2jyWOnT98K6BU5K8F8+TWGz3nct
KtIziw6ubqCPIHbk5LCKsgkg+miF5sRN7BvuKKh2U8dLy56fEpTeiki9YUZSo9ZZ
3857iURhDyW/r5NumlQWfE0ifRbTLmXqRYtp1g3s1/oDTBs72GJxcWTneF6wbcxb
iLqiYuQxIOVGZcDLyz6tUbCgCBm06R1IctP753JOA6txvK+LuEx03slqrfyxhlOo
8FOT1mYGmSO8e5sxNj1tbZtFn0bbW6+W+EBKrxqDHw24qtfZOkJW6BVrK3B1egEg
kwIDAQAB
-----END PUBLIC KEY-----
```
The script below can get plaintext from cipher text. 
``` python
from base64 import b64decode

from Crypto.PublicKey import RSA
# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

f = open("public.pem")
g = open("flag.enc")

key = RSA.importKey(f.read())

n = key.n
e = key.e
d = modinv(e,n-1)
ciphertext =  int(b64decode(g.read()).encode("hex"),16)

print hex(pow(ciphertext,d,n))[2:-1].decode("hex")
# print  d
# plaintext is The empire secret system has been exposed ! The top secret flag is : Flag{S1nGL3_PR1m3_M0duLUs_ATT4cK_TaK3d_D0wn_RSA_T0_A_Sym3tr1c_ALg0r1thm}
# Flag : Flag{S1nGL3_PR1m3_M0duLUs_ATT4cK_TaK3d_D0wn_RSA_T0_A_Sym3tr1c_ALg0r1thm}
```
