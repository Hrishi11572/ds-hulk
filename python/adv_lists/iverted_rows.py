# given a matrix, print the matrix formed from all rows inverted. 

t = int(input())

while t > 0: 
    N, M = map(int, input().split())

    matrix = []

    for i in range(N): 
        matrix.append(list(map(int , input().split())))
    
    for i in range(N): 
        for val in reversed(matrix[i]): 
            print(val, end=" ")
        print("") # print("\n") makes 2 new lines.
    t = t - 1