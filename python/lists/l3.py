'''
Iteration on a list in 3 different ways : 
'''

ls = [1 , 2 , 3 , 4 , 5]


# 1. basic iterartion 
for a in ls : 
    print(a, end=" ")
    
print("\n")

# 2. iteration using indices 
for i in range(len(ls)): 
    print(ls[i], end=" ")

print("\n")    

# 3. using `enumerate`
'''
The enumerate() function simplifies iterating over both the index and the value of a list.
'''

for i, num in enumerate(ls):
    print(f"index:{i} and element:{num}")

    

