a = float(input('First Number: '))
b = float(input('Second Number: '))

try:
    result = a / b
    print('result',result)
except ZeroDivisionError:
    print('Error: Division by Zero')