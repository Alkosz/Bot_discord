import random
from string import printable

def gen_pass(pass_length):
    elements = printable
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password