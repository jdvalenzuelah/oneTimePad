#!/usr/bin/env python3

from bitarray import bitarray
from string import printable
from random import choice

def string_to_bitarray(string: str) -> bitarray:
    array = bitarray()
    array.frombytes(string.encode('utf-8'))
    return array

def get_random_string(len: int) -> str:
    return ''.join([ choice(printable) for _ in range(len) ])


def bitarray_xor(array1: bitarray, array2: bitarray) -> bitarray:
    return bitarray([ array1[i] ^ array2[i] for i in range(len(array1)) ])

def encrypt(string: str) -> tuple:
    key_bitarray = string_to_bitarray(get_random_string(len(string)))
    string_bitarray = string_to_bitarray(string)
    return bitarray_xor(string_bitarray, key_bitarray).to01(), key_bitarray.to01()

def decrypt(enc: str, key: str) -> str:
    enc_bitarray = bitarray(enc)
    key_bitarray = bitarray(key)
    return bitarray_xor(enc_bitarray, key_bitarray).tobytes().decode('utf-8')

def get_file_contents(path: str) -> str:
    content = None
    with open(path, 'r') as file:
        content = file.read()
    return content

def write_to_file(path: str, content: str) -> None:
    with open(path, 'w+') as file:
        file.write(content)

def encrypt_file(path: str) -> None:
    content = get_file_contents(path)
    (enc, key) = encrypt(content)
    write_to_file('enc.txt', enc)
    write_to_file('key.txt', key)

def decrypt_file(msg_path: str, key_path: str) -> str:
    msg = get_file_contents(msg_path)
    key = get_file_contents(key_path)
    return decrypt(msg, key)

if __name__ == '__main__':
    from sys import argv

    if len(argv) < 2:
        print('File to encrypt is required')
    
    if len(argv) == 2:
        encrypt_file(argv[1])
    else:
        print(decrypt_file(argv[1], argv[2]))
