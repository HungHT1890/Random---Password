from string import ascii_lowercase , ascii_uppercase , digits , punctuation
from random import choice

def random_pwd(pwd_length):
    letters = ascii_lowercase + ascii_uppercase + digits + punctuation
    pwd = ''.join(choice(letters) for count in range(pwd_length))
    return pwd
