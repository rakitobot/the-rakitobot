N,M = map(int,input().split())
ans = M
H = list(map(int,input().split()))
for i in range(N):
     
     ans = ans - H[i]

     if ans<0:
        print(i)
        break
if ans>-1:
    print(N)
     