import string
from random import*

characters = string.ascii_letters + string.digits
password = ""
i = 0

while i < 3:
    if i > 0:
        password += "-"
    strHash = "".join(choice(characters) for x in range(5))
    password += strHash
    i += 1

print(password)
