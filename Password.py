import random
import string

def generate_password(length):
    # define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # combine the character sets based on the desired length of the password
    chars = []
    if length >= 4:
        chars.extend(random.sample(lowercase, 2))
        chars.extend(random.sample(uppercase, 2))
        chars.extend(random.sample(digits, 2))
        chars.extend(random.sample(punctuation, 2))
        chars.extend(random.sample(string.ascii_letters + string.digits + string.punctuation, length - 8))
    else:
        chars = random.sample(string.ascii_letters + string.digits + string.punctuation, length)

    # shuffle the characters and join them into a string
    random.shuffle(chars)
    password = ''.join(chars)
    return password

# example usage: generate a 12-character password
password = generate_password(12)
print(password)
