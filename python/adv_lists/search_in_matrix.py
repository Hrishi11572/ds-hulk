# Write your code here

t = int(input())

while t > 0 :
    N, M = map(int, input().split())
    rows=N
    cols=M 
    matrix = []

    for i in range(rows):
        row = []
        val1, val2 = map(int, input().split())
        row.extend([val1, val2])
        matrix.append(row)

    X = int(input())

    p = 0 
    for rows in matrix: 
        for vals in rows: 
            if vals == X: 
                p = 1
                break

    if p == 0 : 
        print("will take number") 
    if p == 1: 
        print("will not take number")
    t = t - 1