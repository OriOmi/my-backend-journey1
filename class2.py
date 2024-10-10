'''
data structures. there are 4 type of dtata structures list topples 
 
list is a type of data structure arranged in order this structure ca have other data types

'''
my_list = ['temi', 'saviour', 'sekinat', 'gozie', 'jide', 'timi', 1, True, False, 17,]
my_list1 = list(range(5))

print(my_list)
print(my_list1)

timi_name = my_list[5]
print('hello ' + my_list[5])
print(f'my name is  {my_list[0]} i  am great indeed. i am   {my_list[9]} clear yrs of age')
print(my_list[-1])

# slicing this is to get a particular range of items or values
print (my_list[2:5])
my_list[6]= 'joy' #used to redeclare an index
print(my_list)
my_list.append(1) # used to add values to the end of a list
print (my_list)
my_list.insert(7, "joel")
print( my_list)
my_list.pop(-1)
print( my_list)
my_list.pop(0) #to remove data
print(my_list)
my_list.insert(0, 'temi') #{to insert} first input for index and second input for data to be inserted 
print(my_list)
print(my_list.clear()) #to clear list

fruit_list = ['pineapple','apple','mango','orange','guava','grapes', 'pear',]
print(fruit_list[2])
fruit_list.insert(7,'corn')
print(fruit_list)
print(fruit_list[2:5])
print(fruit_list.pop(-1)) #when using remove you have to use the data stored in the variable. while pop uses the index.
print(len(fruit_list))
'''
TURPLE
this is the collection of items that ca not be edited
'''
my_turple = ()#empty turple
single_turple = ('joshua',)#sigle turple\
multiple_turple = ('css','html',['js','python','miami'],'1','true')
my_turple2 = (fruit_list,) #converting list to turples
print ( my_turple2)
print ( multiple_turple)
print(multiple_turple[2:5])
print(len(multiple_turple))   
turple1 = (1,2,3)
turple2 = (4,5,6)


turple3 = (1,2,3)
turple4 = (4,5,6)
turple5 = (7,8,9)
print(turple1 + turple2 + turple3 )
fruit_turple = ('pineapple','apple','mango','orange','guava','grapes', 'pear')
list_convert = list(fruit_turple)
print(list_convert)
tuple_fruit = tuple(list_convert)
print(tuple_fruit)
