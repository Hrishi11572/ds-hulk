'''
- You can iterate over a dictionary to process its keys, values, or both.
'''

'''
* Iterating Over Keys
    Use a for loop directly on the dictionary to iterate through its keys.
'''

phy = { 
    "einstein" : "relativity", 
    "maxwell" : "electromagnetism", 
    "galileo" : "relativity"
}

for keys in phy: 
    print(phy[keys])
    
print("")

'''
Iterating Over Values
Use the values() method to iterate through values.
'''

for values in phy.values(): 
    print(values)
    
''' 
Iterating Over Key-Value Pairs
Use the items() method to iterate through key-value pairs.
'''

print("")
for key, value in phy.items(): 
    print(f"keys : {key}, values : {value}")