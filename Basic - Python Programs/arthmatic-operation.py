a=int(input('Please Enter number1: '))
b=int(input('Please Enter number2: '))

if 1<=a<=(10**10) and 1<=b<=(10**10):
    print("Addition of two num: ", a+b)
    print("Subtraction of two num: ", a-b)
    print("Multiplication of two num: ", a*b)
else:
    print('Please Enter valid number.')