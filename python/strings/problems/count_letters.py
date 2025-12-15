'''
Given a string S, build a frequency map for the string. 
'''

# Write your code here

S = input().strip()
cnt = [0] * 26 

for char in S: 
    cnt[ord(char) - ord('a')]+=1

for idx in range(26): 
    if cnt[idx] != 0: 
        print(chr(idx + 97), ":", cnt[idx])
