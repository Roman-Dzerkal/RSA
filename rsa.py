import math
import os
import textwrap


def is_prime(number):
    """ Check is the number prime?
     :number: passed number
     :return: True/false
     """
    prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            break
        elif prime:
            return True
        else:
            return False


def is_coprime(first_num, second_num):
    """ If GCD() of two numbers equal 1, then these numbers are coprime """
    if math.gcd(first_num, second_num) == 1:
        return True
    else:
        return False


def euler_func(p, q):
    return (p - 1) * (q - 1)


# TODO: Unoptimized function. Find another more optimized method!
def find_public_exponent(p, q):
    """ Public exponent is the first coprime number to euler function """
    for e in range(2, euler_func(p, q)):
        if is_coprime(e, euler_func(p, q)):
            return e


def rsa_encrypt(buffer, public_exponent, module):
    """ Main algorithm method.
     :buffer - text string, which will be encrypted
     :public_exponent - public exponent-power
     :module - immediately  module """
    print("Please, wait a few moment. Encrypting... ")
    encrypted_file = open("encrypted.bin", mode="w")

    for i in range(len(buffer)):
        encrypted_file.write(str(binary_pow(ord(buffer[i]), public_exponent, module)) + ' ')
    encrypted_file.close()

    create_public_key_file(buffer, public_exponent, module)
    print("Well done! The file has been encrypted.")


# TODO: Decryption algorithm should be released!!!
def rsa_decrypt(buffer, secrete_exponent, module):
    print(buffer, secrete_exponent, module)


def create_public_key_file(file_name, public_exponent, module):
    key = open(file_name, mode="w")
    key.write("Exponent: " + str(public_exponent) + '\n' + "Module: " + str(hex(module)))
    key.close()


def find_secrete_exponent(public_exponent, old_module):
    """ secrete exponent is invers """
    secrete_exponent, xx, y, yy = 1, 0, 0, 1
    new_module = old_module

    while old_module:
        q = public_exponent // old_module
        public_exponent, old_module = old_module, public_exponent % old_module
        secrete_exponent, xx = xx, secrete_exponent - xx * q
        y, yy = yy, y - yy * q

    secrete_exponent %= new_module
    return secrete_exponent


def read_text_file(file_name):
    text = open(file_name, mode="r")
    file_size = os.path.getsize(file_name)

    buffer = text.read(file_size)

    text.close()
    return buffer


# TODO: Replace on default pow() function
def binary_pow(base, power, module):
    """ Exponentiation by squaring
     :return - result of powering"""
    power = list(bin(power)[3:])
    stack = [base]

    for i in range(len(power)):
        stack.append(stack[i] ** 2 * base ** int(power[i]) % module)

    return stack[-1]


def read_public_key_file():
    public_key_file = open("../public_key.key", mode="r")

    prime_numbers_list = public_key_file.read().splitlines()

    public_key_file.close()
    return prime_numbers_list


def process_text(some_text):
    ord_name_equivalent = ""

    for i in range(len(some_text)):
        ord_name_equivalent += str(ord(some_text[i]))

    ord_name_equivalent = textwrap.wrap(ord_name_equivalent, 8)
    return ord_name_equivalent
