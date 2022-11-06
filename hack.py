import string
from datetime import datetime

import requests

LEVEL = 0

length = 4
chars = ""
if LEVEL in (0, 1, 3, 4):
    chars += string.digits
if LEVEL == 1:
    length = 5
if LEVEL in (2, 3, 4):
    chars += string.ascii_uppercase
if LEVEL == 4:
    chars += "".join(('~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
                      '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'))


def generate_strings(input_string=""):
    if len(input_string) < length:
        for char in chars:
            if len(input_string + char) == length:
                yield input_string + char
            yield from generate_strings(input_string + char)


session = requests.Session()
session.trust_env = False

request_dict = {'level': LEVEL}
password = None
start = datetime.now()

for generated_string in generate_strings():
    request_dict['password'] = generated_string

    r = session.post('http://127.0.0.1:5000/', data=request_dict)
    if r.text == "OK":
        password = generated_string
        break

end = datetime.now()

print(f"Password {password} found after {(end - start).total_seconds()} seconds.")
