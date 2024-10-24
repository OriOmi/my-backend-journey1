'''
FUNCTIONS
functions are blocks of organised re-usable code

'''
'''def name (jeremy):
  message = f'hello {jeremy}'
  return(message)

print( name('joel'))
print( name('jeremy'))
print( name('OriOmi'))
print( name('bolu'))
print( name('cress'))

def add (a,b):
  addition = a + b
  return(addition)

print(add (5,7))'''

#CLASSWORK
'''
Write a function that checks if a number is even or odd
write a function that sums all the number in a list
write a function that gets the max number in a list
write a function that calculates the area of a circle
wrie a function to write a common difference between two list 
wrie a function tahts perform a dice rolling game
'''

def number_character_checker (int) :
  if int % 2 == 0 :
    print ('this number is an even number')
  else :
    print('this is an odd number')
  return

number_character_checker(2)

import math
def area_circle(radius):
  area =(radius ^ 2) *math.pi
  print (area)
  return
  


import random
def dice_roll (dice) :
  dice = random.randrange(1,7)
  print(dice)
  return

dice_roll (any)

#CORRECTION

def total(list_of_numbers):
  return sum(list_of_numbers),max(list_of_numbers)
print(total([1,2,3,4,5,6,6,7,8]))

def spin_game () :
  return print(random.choice(['0.1btc','100k','N20']))
spin_game()


def shop(cash_at_hand,item_price) :
  if cash_at_hand>item_price:
    print ('Transaction successful')
  else :
    print('Insufficient funds')
  print(f'balance = {cash_at_hand - item_price}')
  return

shop(12000000, int(input('product_price')))

#or

def shop():
  cash_hand = 100
  item_price= int(input('price of item'))
  if cash_hand >= item_price:
    balance= cash_hand - item_price
    print (f'Transaction Susseccful your')
    print(f'balance = {balance}')
  else :
    print('Insufficient balance')
    print(f'balance = {balance}')

user = {}
 
def reg_of_user ():
  user['username'] = input('your username')
  user['password'] = input('password')
  if user['username'] in user:
    print('user name exist')
    user['username'] = input('enter a valid username')
  else :
    print('registration done')