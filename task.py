'''classwork
create a function that picks a random item from a list
create a function that checks if a number is even or odd
create a function that gives the cube of a number
create a function that checks if a letter is vowel or consonant
'''

def random_picker(lis):
 import random
 random.choice (lis)

def even_or_odd(number):
 if number %2 == 0:
  print ('odd number')
 else :
  print('even number')

def cube_number(number):
  print (number*number*number)


def letter_confirmer(letter):
  if letter == any(['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']):
    print('consonant letter')
  else :
    print('vowel letter')

cube_number(7)