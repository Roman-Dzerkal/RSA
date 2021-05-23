import rsa
import os

text_buffer = rsa.readSourceFile("source_text.txt")
text_buffer = rsa.process_text(text_buffer)

p = int(input("Enter the first prime number: "))

if not rsa.isPrime(p):
    print("This number is not prime. Try next time.")
    os.abort()

q = int(input("Enter the second prime number: "))

if not rsa.isPrime(q):
    print("This number is not prime. Try next time.")
    os.abort()

# [public_exponent; module] - Public key
module = p * q
print(module)

public_exponent = 8191
print(public_exponent)
# rsa.rsaEncrypt(text_buffer, public_exponent, module)

# [secrete_exponent; module] - Private key
secrete_exponent = rsa.findSecreteExponent(public_exponent, module)
print(secrete_exponent)