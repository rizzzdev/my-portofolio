import random
import os
import string

def clear():
    os.system('cls')

def create_id(untuk):
    return untuk + '-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))

def encode_string(str):
    tanda_baca = ['`', '~', '!', ' ', '@', '#', ',', '.', ':', ';', '?', '/', '%', '(', ')', '-']
    for i in tanda_baca:
        str = str.replace(i, '')
    return str


