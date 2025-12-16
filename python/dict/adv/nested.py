# nested dictionary 

departments = dict(
    IT=dict(manager="John", employees=10),
    HR=dict(manager="Alice", employees=5)
)
print(departments)

# Iteration 
for deps, details in departments.items():
    print(f"{deps}'s details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

'''
prints : 
    IT's details:
    manager: John
    employees: 10
    HR's details:
    manager: Alice
    employees: 5
'''