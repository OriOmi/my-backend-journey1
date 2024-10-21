import random
coin_selection =['Heads','Tails'] 
user_selection = None

while user_selection != 'quit':
  user_selection = input('Heads or Tails')
  computer_selection = random.choice(coin_selection)
  if user_selection == 'quit':
    print (f'game exited')
    break
  if computer_selection != user_selection:
    print (f'haha you lose you pick {user_selection}. Outcome:{computer_selection}')
  else:
    print(f'Okay okay you win you pick {user_selection}. Outcome:{computer_selection}')
  

  