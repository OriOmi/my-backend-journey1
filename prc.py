

'''try:
  f = open('class6 folder\Assigment7.py\simpledatbase.py')
except FileNotFoundError as n:
  print(n)
else:
  print(f.())
  f.close'''

#THIS CODE COLLECTS INPUT FROM USER AND ADDS THEM TO A LIST UPCOMING UPDATES WOULD HELP USER GET AVERAGE SUM AND LENGTH OF ALL INPUTS 

def average_of_numbers () :
  lis=[]
  enter=(input('enter a number '))
  try :
    if (type(enter)== str) :
      Exception
  except Exception :
    print('Error! Input an Integer')

  entry = lis.append(enter)
  if enter == 'done':
    print ('empty set')
  while enter != 'done':
    enter=(input('enter a number '))
    entry = lis.append(enter)
    if enter == 'done' :
        lis.remove('done')
        print(lis)    
        print(max(lis))
        print(min(lis))
        '''print(sum(int(lis)))
        print(len(lis))
        print (sum(lis)/len(lis))'''
    try:
      if type(enter)== str :
        raise Exception
    except Exception :
      print('Error! Input an Integer.')
    

average_of_numbers()
      

      
  