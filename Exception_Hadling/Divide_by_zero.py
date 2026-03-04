def calculate(a, b):
    return a/b
try:
    a = int(input('Enter first value : '))
    b = int(input('Enter second value : '))
    print(calculate(a, b))
except ZeroDivisionError:
    print('Divisior can not be 0 ')  
except ValueError:
    print('Give numbers only ')    