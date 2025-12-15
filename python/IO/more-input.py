# more on input function 

value = input("Enter the number! ")
print(value)
print(type(value))

'''
FUNC input(), always returns a string, despite the fact that the input was an integer. 
'''


# 2. Conversion to float() and int().

fvalue = float(input("Enter the Float value "))
print(fvalue)

invalue = int(input("Enter the int value "))
print(invalue)


# 3. Handling multiple inputs using .split()

three = 3
x, y, z = input(f"Enter {three} values ").split()
print(f"The input values are {x}, {y}, {z}")