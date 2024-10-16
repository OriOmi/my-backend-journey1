#Numbers and operators
a = 6 
b = 5
d = a + b
print( f'the addition of a and b is {d}')

a1 = 2
b1 = 5
d1 = a1 * b1
print(f'the multiplication of a and b is {d1}')

a2 = 9 
b2 = 5
d2 = a2 / b2
print(f'the division of a and b is {d2}')

a3 = 12
b3 = 5
d3 = a3 // b3
print(f'the remainder of the division of a and b is {d3}')

a4 = 8
b4 = 5
d4 = a4 - b4
print(f'the subtraction of a and b is {d4}')


#comparison operators
#Equal
y= a==b
print(f' a and b are equal... {y}')

y= a > b
print(f' a and b are equal... {y}')

m= a < b
print(f' a and b are equal... {m}')

i = a <= b
print(f' a and b are equal... {i}')

j = a >= b
print(f' a is less th... {j}')


if(a>b) : {print('yes a is greater than b') } 
else:{ print("no b isn't greater than a ")} 

# LOGICAL OPERATORS

Y = 6 == 6
z = 6 > 6
print(y)
print( z)
print( z and y)
print( z or y)
print (not y )
g = 7
g+=8
print(g)

#Conditional statements
'''
if condition:
    Code'''

if(a>b) : {print('yes a is greater than b') } 
else:{ print("no b isn't greater than a ")} 

# Write a computer program that would check if your account balance is sufficient enough for a cash trasaction
'''initial_account_balance= 4382900
withdrawal_amount= int(input( 'Input  withdrawal Amount'))
account_balance = initial_account_balance - withdrawal_amount
if (initial_account_balance >= withdrawal_amount) :   #CONDITIONAL STATEMENTS
        print( 'withdrawal processing....')
        print( 'withdrawal successful')
       
else :
        print('insufficient funds')
if (initial_account_balance< withdrawal_amount) :
      print (f'you account balance is {initial_account_balance}')
else :
       print(f'you account balance is {account_balance}') 

Password = str(input( 'input password'))
confirm_Password = str(input('Confirm Password'))

# Write a computer program that would check if your account 
if (confirm_Password == Password):
       print( 'Congratulations you have been successfully signed up')
else:
       print('password not matching')





User_Biodata = {}

User_Biodata['username']= input('input your username ') #REFERENCE CLASS3
User_Biodata['password']= input('input password ')#REFERENCE CLASS3
User_Biodata['Confirm password']= input('confirm password ')#REFERENCE CLASS3
User_Biodata['email']= input('input email ')#REFERENCE CLASS3
User_Biodata['work ID number']= input('input work id number ')#REFERENCE CLASS3
User_Biodata['Country of residence']= input('input country of residence ')#REFERENCE CLASS3
if (User_Biodata['password'] == User_Biodata['Confirm password']):  # THIS IS USING CONDITIONAL EQUALS TO FOR INPUTS
       print( 'Congratulations you have been successfully signed up')
       print(User_Biodata)
else:
       print('password not matching')
       print('retry')
'''


'''
Assignment
|||
write a pyhton code to check if a python code is even or odd
write a python code for a grade checker (ckeck a students grade based on their score)
write python code to check if a number is positive negative or zero
write python to check if a year is a leap year
'''
#ASSIGMENT
#1
'''
number = int(input('imput number to check if it is an even or odd number '))
intermidiary1 = number/ 2
intermidiary = round(intermidiary1)

if (intermidiary * 2 == number):
       print(f'{number} is an even number') 
else :
       print(f'{number} is an odd number') 



'''
             

'''
grade = int(input('what is your grade number'))   
if (grade >= 70) :
       print ( 'congratulations you have an A')
elif (grade >= 60 and grade < 70 ) :
       print ( 'congratulations you have a B')
elif (grade >= 50 and grade < 60 ) :
       print ( 'KAI you have a C')     
elif (grade >= 45 and grade < 50 ) :
       print ( 'KAI you have a D')
elif (grade >= 40 and grade < 45 ) :
       print ( 'sorry you have a E')
elif (grade >= 0 and grade < 40 ) :
       print ( 'Unfortuately you are coming back next year')                  

'''
'''
number_input = int(input( 'what  number do you want to check its characteristics'))
if (number_input == 0) :
       print(f'{number_input} is zero')
elif(number_input > 0 ) : 
       print(f'{number_input} is a positive number') 
elif(number_input < 0 ) : 
       print(f'{number_input} is a negative number')   '''

year = int(input('which year do you want to confirm if it is a leap year'))
output1 = round(year/4)
output2 = round((year+2))
output3 = round(output2/4)
 

if (output1*4 == year and (output3*4)-2 == year ) :
       print(f'year {year} is a leap year')
else : 
       print( f'year {year} is not a leap year')        
         