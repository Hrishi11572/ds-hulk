''' 
1. Membership Tests
Check if a Key Exists
    Use the `in` operator to check if a key exists in a dictionary. Use `not in` to check if it does not exist.
'''

phy = {
    "einstein" : "Relativity", 
    "maxwell" : "einstein", 
    "boltzmann" : "statistical thermodynamics"
}

print("einstein" in phy) # True 
print("faraday" not in phy) # True 