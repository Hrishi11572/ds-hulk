# List , Dict , Set are mutable data types 

my_list = [1 , 2 , 3]
my_list[0] = 10
print(my_list)

# tuple, string , int - float are IMmutable 

my_tuple = (1, 2 , 3)

''' This throws error !'''
# my_tuple[0] = 12
# print(my_tuple)


# the int , float case

value = int(45)
value = 4

# print(value) .. prints 4, this is not the example of IMmutability, it's of reassignability. 
# the correct example is value[0]

# print(value[1]) .. throws ERROR 


'''
The COMPLEX data type 
'''

z = 0.5 + 2j
print(z)
print(type(z))