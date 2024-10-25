# This is a simple sign up database
print('This is a simple sign up database')
User_Database = {
  'Username' : 'jeremy',
}
  

def User_Registration () :
  definition1 = User_Database['Username'] # at this line instace definition1 = jeremy {importat lie of code }
  User_Database['Username']= definition2 = input('Input Username ') # at this second line instance definition2 = new username
  while  definition2 == definition1: # if definition2 == definition1 code continues to run until else statement(reak statement)
      if definition2 == User_Database['Username']:
        print('Username already exists!') #code prints this if username already exists 
        User_Database['Username']=input('Input Another Username ')
      else: #if userame doesnt already exist it automatically exits functiion cause of break statemets
        break 
    
  User_Database['Password']=input('Input Password')
  print('Congratulations you have been successfully Registered')
  
User_Registration()

print(User_Database)

  
  
