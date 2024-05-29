import string
from itertools import product


for passcode in product(string.digits+string.ascii_letters+string.punctuation,repeat=3):
        print(*passcode)
        