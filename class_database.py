users = {
}

def register ():
  user_name = input ('enter a username')
  if user_name in users :
    print('pick another user name')
  full_name= input('enter your full name')
  username = input('enter your username')
  password1 = input ('enter your password')

  
  users['user_name'] = {'User_name' : username,'fullname': full_name, 'passkey':password1}
  print(users)
  return


#login function

def login ():
  if not users :
    print ('user has not been registered')
  userName = input('enter your full name')
  password = input('enter your password')
  if users.get(register.__get__(users['user_name']['Username']))== userName and users.get(register.__get__(users['user_name']['passkey']))==password: # if users.get(userName) and users ['user_name']['password'] ==password:
    print(f"welcome{users['user_name']['fullname']}")
    return

  

def main ():
  current_user = None
  while True:
    print('/n option register login logout')
    choice = input('input an option').lower()

    if choice == 'register':
      register()
    elif choice == 'login':
      login()
    elif choice == 'quit':
      print('exiting program')
      break
    else:
      print('invalid input')

main()