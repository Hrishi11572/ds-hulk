'''
Creating a 2-D list of size 3 * 3 
'''

rows , cols = 3, 3

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i*j)
    matrix.append(row)

print(matrix)


'''
# Taking Variable-Size 2D List Input
    - If the rows can have different numbers of columns, allow the user to input the size dynamically.
'''

rows = int(input("Enter the number of rows: "))
matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter elements for row {i+1}, separated by spaces: ").split()))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)
