
'''
D = {'a': 1, 'c': 3, 'b': 2}
Ks = list(D.keys()) 
print(Ks)
Ks.sort()
print(Ks)
for key in D: # Iterate though sorted keys]
       print(key, '=>', D[key])
'''
'''
x = 4
while x > 0:
       x -= 1
       print('spam!' * x)
       x -= 1
M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists
     [4, 5, 6], # Code can span lines if bracketed
     [7, 8, 9]]
print(M)
col2 = [rOw[1] for rOw in M] 
print(col2)

hours = int(input('how many hours have you worked this week' ))
pay_per_hour = 10
pay= hours  * pay_per_hour
if (hours< 40) : 
       print(f'your pay for hours worked is {pay}')
else :
       pay =1.5* (((hours - 40))*pay_per_hour ) + pay 
       print(f'your pay for hours worked is {pay}')
'''

def print_twice(bruce) :
       print(bruce)
       print(bruce)

'''
loops
for loops this is used for repitition 
'''

successful = False

spam = 'spam'
for character in spam:
       print_twice('sat')
       if successful :
              print('this is a spam message')
              break 
else: 
       print(' we do not wat to send you a spam message more than once')       


#nested loops

for x  in range(5):
       for y in range(12) :
              print(f'{x}, {y}')


fruit = ['banana','mango','apple']
for fruits in fruit:
       print_twice('set')

count = 0
for number in range(1,  10):
       if number % 2 == 0:
              count+=1
              print(number)

print(f'we have {count} even numbers')

'''for number in range(1,10000) :
       if number%2 != 0:
              count+=1
              print (number)
print(f'we have {count} odd numbers'''

for number in range(1,10) :
       if number%2 != 0:
              count+=1
              print (number)
print(f'we have {count} odd numbers')


#WHILE LOOPS
x = 0

while x< 10:
       
       print (x)
       x+=1