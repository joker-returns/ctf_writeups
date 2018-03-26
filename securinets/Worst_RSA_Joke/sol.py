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


