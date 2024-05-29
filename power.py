def pow(x,y):
    if y==0:
        return 1
    else:
        return x*pow(x,y-1)
    
print(pow(5,3))