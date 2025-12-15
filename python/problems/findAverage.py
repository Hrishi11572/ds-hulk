# Write your code here

N = int(input())
ls = list(map(float , input().split())) # for taking input as 2.0 4.5 9.7

# averaging function 

def findAvg(ls : list)->float: 
    avg = sum(ls)/len(ls)
    return avg 

print(f"{findAvg(ls):.7f}") # print till 7 decimal points 