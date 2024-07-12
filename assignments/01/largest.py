a = int(input('Enter 1st No.:'))
b = int(input('Enter 2nd No.:'))
c = int(input('Enter 3rd No.:'))

result = a if (a > b and a > c) else (b if b > c else c)
print(result)
