from string import digits
from itertools import product


secretcode=('1','6','4','5')

for passcode in product(digits,repeat=4):
    if passcode == secretcode:
        print('code is',*passcode)
