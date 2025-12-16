# count the number of increasing subarrays of a given array 

t = int(input())

while t > 0 : 
    N = int(input().strip())
    arr = list(map(int, input().split()))

    p1 = 0 

    ans = 0 

    while p1 < N: 
        p2 = p1+1
        while p2 < N and arr[p2] >= arr[p2-1]: 
            p2 += 1

        l = p2 - p1 
        ans += l * (l + 1)//2 
        p1 = p2 

    print(ans)
    t -= 1 