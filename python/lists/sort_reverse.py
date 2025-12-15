'''
sorted(): Returns a new sorted list, leaving the original list unchanged.

list.sort(): Sorts the list in place.

reversed(): Returns a reversed `iterator` (creates a new sequence).

list.reverse(): Reverses the list in place.
'''


# SORTING 
ls = [9, 2, 4 , 9, 10, 0 , 8 , 4, 6 , 7, 12]
new_ls = sorted(ls) # -- creates new_list 

print(ls, new_ls)

ls.sort()

print(ls)

# REVERSING 

ls = ["apple", "banana", "mango", "pomegranate"]
print(ls)

rev_ls = reversed(ls)
print(rev_ls) # -- not a list 

rev_ls = list(rev_ls)
print(rev_ls)

ls.reverse()
print(ls)