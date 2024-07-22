N,S,K = map(int,input().split())
ans = 0
for i in range(N):
    P,Q = map(int,input().split())
    ans = ans + P*Q
if S>ans:
     print(ans+K)
else:
     print(ans)

