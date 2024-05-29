import string
from itertools import product

code=('m','@','1')

for passcode in product(string.digits+string.ascii_letters+string.punctuation,repeat=3):
    if passcode ==code:
        print(*passcode)
        