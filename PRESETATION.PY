def calculator ():
  print('this is a simple calculator that performs double input calculations')
  number1 = float(input('enter the first  integer '))
  operand = input('select operand that ypu wish to implement')
  number2= float(input('enter the second  integer '))
  if operand == '+' :
    print(number1 + number2)
  elif operand =='-':
    print(number1 - number2)
  elif operand =='/':
    print(number1 / number2)
  elif operand =='*':
    print(number1 * number2)
    

calculator()