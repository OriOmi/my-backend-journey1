'''
set
this is an unordered collection of unique uneditable (element) they are defined using curly braces {}

'''
set_of_numbers = {1,2,3,4,5,6,67,7,7,7,8,9,7,7,5,4,33,5}
print(set_of_numbers)
list_of_numbers = [2,4,5,6,7,7,778,88,3,24]
print(list_of_numbers)
print(set(list_of_numbers))
set_of_numbers.add('joy')
print(set_of_numbers)
print(set_of_numbers.__len__())

print(set_of_numbers)
print(set_of_numbers.clear())

igbo_foods = {'egusi', 'bitter leaf', 'baanga', 'rice', 'beans'} 
yoruba_foods = {'rice', 'beans', 'ewedu', 'salad', 'fish','amala', 'egusi'}
union_foods = yoruba_foods | igbo_foods
print (union_foods)
interset_set = yoruba_foods & igbo_foods
print (interset_set)
signed_up_user = {'user1','user2','user3','user4','user5'}
logged_in_users = {'user3','user4','user4'}
active_users = signed_up_user & logged_in_users
print(active_users)

'''dictionary
this is an unordered collection of items that stores data in key value pairs
'''

joy_details ={
    'username' : 'joy',
    'password' : 5229,
    'email' : 'joy419@gmail.com'
}
joy_name = joy_details['username']
joy_password = joy_details['password']
joy_email = joy_details['email']
print(joy_name)
print(joy_password)
print(joy_email)

joy_details['id_name'] = 419 #used for adding variables or editing variables in a dictionary
print(joy_details)
joy_details['password'] = 9323872865 #used for adding variables or editing variables in a dictionary
del joy_details['email']
print(joy_details)

