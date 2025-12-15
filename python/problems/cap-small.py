# Write your code here

X = input().strip()

X = X[0]


if ord(X)-ord('0') in range(1,10): 
    print("IS DIGIT")
else : 
    print("ALPHA")
    if ord(X) >= 65 and ord(X) <= 90 : 
        print("IS CAPITAL")
    elif ord(X) >=97 and ord(X) <= 122: 
        print("IS SMALL")