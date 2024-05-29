

def larger(a,b):
    if a>b:
        print(f'{a} is larger than {b}')
    elif a<b:
        print(f'{b} is larger than {a}')
    else:
        print(f'{a} and {b} are equal')

def largest(a,b,c):
    max=-1000
    if a>max:
        max=a
    if b>max:
        max=b
    if c>max:
        max=c
    return max         

print(larger(3,7))
print(largest(6,2,9)) 