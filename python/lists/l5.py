# more on lists 

'''
Adding elements to existing list -

    append(): Adds a single element to the end of the list.
    extend(): Adds multiple elements from another iterable (e.g., list, tuple) to the end of the list.

'''

ls = ["apple", "mango"]
ls.append("banana")
ls.append("orange")

ls1 = ["grape", "pomigranade", "kiwi"]

# pre-extension 
print(ls)

ls.extend(ls1)

# post-extension 
print(ls)


''' 
Inserting Elements - 
    insert(index, element): Inserts an element at a specific position.
'''

fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # Outputs: ['apple', 'banana', 'cherry']

'''
Removing Elements:

    remove(value): Removes the first occurrence of the specified value.
    pop(index): Removes and returns the element at the specified index (default is the last element).
    clear(): Removes all elements from the list.

'''

ls.clear()
print(ls)