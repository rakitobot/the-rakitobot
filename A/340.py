A,B,D = map(int,input().split())
ans = A
S = (B-A)/D-1
print(A,end=" ")
for i in range(int(S)):
    ans = ans  + D
    print(ans,end=" ") 
if A == B:
    exit()
print(B)
