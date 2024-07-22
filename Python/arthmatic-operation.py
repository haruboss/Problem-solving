def arthmatic_operation():
    num1 = float(input("Please Enter Number 1: "))
    num2 = float(input("Please Enter Number 2: "))
    
    if number_is_valid(num1, num2):
        return {'addition':num1 + num2, 'subtraction':num1 - num2, 'multiplication': num1 * num2 }
    return "Please enter a valid number."
    
def number_is_valid(number1, number2):
    return 1 <= number1 <= (10 ** 10) and 1 <= number2 <= (10 ** 10)
   
    
result = arthmatic_operation()
print(result)