'''loops simply allows you to repeat a block of code multiple times

for loops are used when u know before hand how many times you want to repeat an action


'''
'''FOR LOOPS SYNTAX
for variable in sequence :
      CODE....
'''

# while loops operates under conditions.

'''names = ['GOH','temi','jeremy','oriomi']

for name in names :
  print(f'hello {name}')

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for letters in alphabets :
  print(letters)

my_love = 'i love python'
for numbers in range (10):
  print(my_love)'''

'''about_me = {
   'name' :'Falade Temiloluwa',
   'age' : '17',
}
 
for key,value in about_me:
  print(f'{key}is {value}')'''

'''for numbers in range(2,100):
  if (numbers %2 ==0 ) :
    print(numbers)'''

classes = ['class1', 'class2', 'class3'] 
students = ['student1', 'student2','student3']

for classs in classes :
  for rep in students :
    print(classs, rep)


sections = [1, 2, 3]
Assigned = ['A', 'b','c']

for assignment in Assigned :
  for section in sections :
    print(assignment, section)

multiplier1 = [1, 2, 3,4,5,6]
multiplier2 = [1, 2,3,4,5,6,7,8,9,10,11,12]

for multiplier in multiplier1 :
  for mult in multiplier2 :
    print( f'{multiplier} x {mult} =  {multiplier * mult}')

records = [
  {'username':'OriOmi', 'password': 24657},
  {'username': 'Jeremy', 'password': 3274},
  {'username':'temz' , 'password': 28942},
                    ]

for record in records:
  for key,value in record.items():   #record.items() represents the items under the dictionary
    print(f'{key}= {value}')


count = 0
while count < 10 :
  print("i love you")
  count+=1

count = 0
while count <10:
  count+=1
  print(count)