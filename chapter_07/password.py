from string import ascii_lowercase
import itertools


def every_password(length):
    for s in itertools.product(ascii_lowercase, repeat=length):
        print("".join(s))
