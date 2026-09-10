# EVEN RSA CAN BE BROKEN???
> This service provides you an encrypted flag. Can you decrypt it with just N & e?
> HINT:
> 1. How much do we trust randomness?
> 2. Notice anything interesting about N?
> 3. Try comparing N across multiple requests

we are given a file `encrypt.py`
```python
from sys import exit
from Crypto.Util.number import bytes_to_long, inverse
from setup import get_primes

e = 65537

def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)

def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

def main(flag):
    pubkey, _privkey = gen_key(1024)
    encrypted = encrypt(pubkey, flag) 
    return (pubkey[0], encrypted)

if __name__ == "__main__":
    flag = open('flag.txt', 'r').read()
    flag = flag.strip()
    N, cypher  = main(flag)
    print("N:", N)
    print("e:", e)
    print("cyphertext:", cypher)
    exit()
```
So first of all we need to understand how RSA works:
1. A message \(m\) is converted into an integer representation.
2. Encryption is performed using the public exponent \(e\) and modulus \(N\):
   
   C = m^e mod N
4. The ciphertext \(C\) is transmitted to the receiver.
5. Decryption uses the private key \(d\) and modulus \(N\):
   
   m=C^d mod N
6. The private key \(d\) satisfies:
   
   e⋅d≡1(modφ(N))
   
   where \(phi(N) = (p-1)(q-1)\) is Euler’s totient function.

based on the hint we should use the weak randomness in prime generation, but because the N is not a big number, so instead we find the p and q by using that we can just use factordb, so heres the flag

[Solution](soln.ipynb)

FLAG: `picoCTF{tw0_1$_pr!m305af7255}`
