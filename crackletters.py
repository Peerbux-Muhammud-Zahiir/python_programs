from string import ascii_letters
from itertools import product


code=('a','f','h','r')

for passcode in product(ascii_letters,repeat=4):
    if passcode==code:
        print('Your code is ',*passcode)
