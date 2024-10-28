
def calculator() :
  print('This is a calculator that performs simple double input calculations')
  input1= int(input('input 1'))
  input2= int(input('input 2'))
  print('what do you want to do with these numbers Add Sutract Multiply Divide')
  operand = input('')
  if operand == '+' :
    print(input1+input2)
  elif operand == '*':
    print(input1*input2)
  elif operand == '/':
    print(input1+input2)
  elif operand == '-':
    print(input1-input2)
  return

calculator()