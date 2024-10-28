import random
random_number = random.randrange(1,3)
user_input = None
if (random_number <1 and random_number>= 0):
    computer_move = 'rock'
elif (random_number <2 and random_number>= 1):
    computer_move = 'paper'
else :
  computer_move = 'scissors'

  
while user_input != 'quit' :
  user_input = input('Rock Paper Scissors')
  if user_input == 'quit' :
     print('game exited')
     break

  if user_input == computer_move:
    print(f'tie you pick {user_input} computer picked {computer_move}')
  elif user_input == 'paper' and computer_move == 'rock' or user_input == 'rock' and computer_move == 'scissors' or user_input == 'paper' and computer_move == 'rock' :
    print(f'you win you pick {user_input} computer picked {computer_move}') 
  elif user_input == 'rock' and computer_move == 'paper' or user_input == 'paper' and computer_move == 'scissors' or user_input == 'scissors' and computer_move == 'rock' :
     print(f'you lose computer picked {computer_move}. you picked {user_input}')
  else :
    print(f'Invalid Input')