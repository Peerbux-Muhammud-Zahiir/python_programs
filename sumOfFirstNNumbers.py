def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
    
print('Sum of first 10 numbers is : ',sum(10))
print('Sum of first 100 numbers is : ',sum(100))

