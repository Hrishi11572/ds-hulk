# Lektion on data types (the new ones)


# Complex
var1 = 0.5 + 5.8j
print(var1, type(var1))

# List 
var2 = [8, 1, 2, 9]
print(var2, type(var2))

# Tuple 
var3 = (9, 7, 1)
print(var3, type(var3))

# range 
var4 = range(5)
print(var4, type(var4))

# Dictionary 
var5 = {"name": "John", "age": 25}
print(var5, type(var5))

# Set 
var6 = {1 ,2 , 3, 6, 7}
print(var6, type(var6))

# frozenset : IMMutable version of set 
var7 = frozenset({1, 6, 9, 0, 23})
print(var7, type(var7))

# None 

x = None 
print(x , type(x))

# Type Conversion in Python 

x = 5 
y = float(x)
z = str(x)

print(x , type(x))
print(y , type(y))
print(z, type(z))