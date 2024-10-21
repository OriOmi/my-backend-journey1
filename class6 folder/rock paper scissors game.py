import random
choice = ['rock','paper','scissors']
players_choice = None

while players_choice != 'quit' :
  players_choice = input('enter rock paper scissors or (quit)')
  if players_choice == 'quit':
    break
  computer_choice = random.choice(choice)
  print(f'comupter chooses {computer_choice}')
  if players_choice == computer_choice:
    print('tie')
  elif players_choice == 'rock' and computer_choice == 'scissors' or players_choice and computer_choice =='paper' or players_choice == 'rock' and computer_choice=='paper':
    print( 'you win')
  else:
    print ('you lose')