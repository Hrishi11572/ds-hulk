K, S = map(int , input().split())

ans = 0 
for i in range(0, K+1):
    T = S - i 
    if T < 0 :
        break 
    if T <= K : 
        ans += T + 1
    elif T > K and T <= 2*K: 
        ans += (2*K - T + 1)

print(ans)

'''
K = 9 S = 4 
t = 4 
ans += 5 
t = 3
ans += 4 
t = 2 
ans += 3 
t = 1 
ans += 2 
t = 0 
ans += 1 
'''