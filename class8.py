'''assignment
create a function that squares a number
create a function that finds the average of a group of numbers in a list
create a function that reverses a list
create a function that converts a string to an upper case
create a function that removes duplicate from a list
creates a function that joins two list
create a quiz using functions
create a function that stores login and logout
'''
'''
def sqr (number) :
  return print(int(number)**2)'''

'''def average (list):
  add = (sum(list))/len(list)
  print (add)'''

'''def stringUpperCoverter (strin):
  print (strin.upper())

def stringUpperCoverter (strin):
  print (strin.lower())'''

'''def dupli(oy):
   return list(set(oy))
'''
'''
def listCombiner (list1,list2) :
  print(list1+ list2)
  return
listCombiner([1,2,3,4],[3,6,8,9])
'''
'''def list_reverser (lis):
  print(lis[::-1]) # [::-1] this is used to reverse a list
  return

list_reverser([1,2,3,4,5])'''
'''
def quiz () :
  question1 = input('what is left after a collapsed neutron star A blackhole B white dwarf')
  if question1 == 'A' :
    print (1/1)
  if question1 == 'B' :
    print ('wrong')
  else :
    print('input either A or B')

quiz()'''

'''User_Database = {
  'Username' : 'jeremy',
}
  

def User_Registration () :
  User_Database['Username']= definition2 = input('Input Username ')
  while  definition2 == User_Database['Username']:
    if definition2 == User_Database['Username']:
      print('Username already exists!')
      User_Database['Username']=input('Input Another Username ')
    else:
      break
    
  User_Database['Password']=input('Input Password')
  print('Congratulations you have been successfully Registered')
  print(User_Database)
  
User_Registration()

print(User_Database)

  
'''

user = {}
def register() :
  user_name = input ('enter your username ')
  if user_name in user :
    print(' user name already exists')
  return
passkey = input('enter your password')
user ['username']= passkey
print('registration done')





