def compute(a,b,o):
    if o=='+':
        return int(a)+int(b)
    elif o=='-':
        return int(a)-int(b)
    elif o=='*':
        return int(a)*int(b)
    elif o=='/':
        return int(a)/int(b)
    else:
        print('Invalid operator')
        return -1

print(compute(3,4,'*'))