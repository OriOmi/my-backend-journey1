import random
target_number = random.randrange(1,10)
user_guess = None
while user_guess != target_number:
  user_guess = int(input(' Kindly enter any random number from 1 to 10'))
  if user_guess < target_number:
    print ('Hint : choose a bigger number')
  elif user_guess > target_number:
    print ('Hint : choose a lesser number')
  elif user_guess == target_number:
    print(f'hooray the number guessed is {target_number}')