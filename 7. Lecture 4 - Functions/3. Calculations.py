def calculator(operator, num1, num2):
    if operator == 'multiply':
        return  num1 * num2
    elif operator == 'divide':
        return  int(num1 / num2)
    elif operator == 'add':
        return  num1 + num2
    elif operator == 'subtract':
        return  num1 - num2
    else:
        return 'Invalid operator'

operator = input()
num1 = int(input())
num2 = int(input())

print(calculator(operator, num1, num2))


#### Second way ####
#
#def calculator(operator, num1, num2):
#    return {
#        'multiply' : num1 * num2,
#        'divide' : int(num1 / num2),
#        'add' : num1 + num2,
#        'subtract' : num1 - num2
#    }.get(operator, 'Invalid operator')
#
#operator = input()
#num1 = int(input())
#num2 = int(input())
#
#print(calculator(operator, num1, num2))
#