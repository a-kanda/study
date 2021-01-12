# coding: utf-8
# Here your code !
A, B, X = map(int, input().split())
 
small = 0
big = 1000000001
result = 0
 
while(big-small > 1):
    t = A * (big+small)//2 + B * len(str((big+small)//2))
    
    if X > t:
        small = (big+small)//2
    elif X < t:
        big = (big+small)//2
    else:
        print((big+small)//2)
        exit()
    
 