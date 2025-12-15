# Write your code here

N , Q = map(int, input().split())
S = input()

while Q > 0: 
    query = input()
    if query == "pop_back": 
        str_list = list(S)
        str_list.pop(-1)
        S = "".join(str_list)
    elif query == "front": 
        print(S[0])
    elif query == "back": 
        print(S[-1])
    elif "sort" in query: 
        t = query.split(" ")
        l = int(t[1])
        r = int(t[2])

        if l > r :
            # swapping  
            c = l
            l = r 
            r = c  
        
        l = l - 1
        r = r - 1 
        str_list = list(S)
        new_str_list = sorted(str_list[l:r+1])
        str_list[l:r+1] = new_str_list
        S = "".join(str_list)
    elif "reverse" in query:
        t = query.split(" ")
        l = int(t[1])
        r = int(t[2])

        if l > r :
            # swapping  
            c = l
            l = r 
            r = c  
        
        l = l - 1 
        r = r - 1 

        str_list = list(S)
        new_str_list = reversed(str_list[l:r+1])
        str_list[l:r+1] = new_str_list    
        S = "".join(str_list)
    elif "print" in query: 
        t = query.split(" ")
        pos = int(t[1])

        print(S[pos-1])
    
    elif "substr" in query: 
        t = query.split(" ")
        l = int(t[1])
        r = int(t[2])

        if l > r :
            # swapping  
            c = l
            l = r 
            r = c  
        
        l = l - 1 
        r = r - 1 

        print(S[l: r + 1])
    
    elif "push_back" in query:
        t = query.split(" ")
        x = t[1]

        str_list = list(S)
        str_list.append(x)

        S = "".join(str_list)
    Q = Q-1
