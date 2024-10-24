User_Database = {
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
  
User_Registration()

print(User_Database)

  
  
