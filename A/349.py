N = int(input())
A = list(map(int,input().split()))
ans = 0 
ans = 0
for i in range (N-1):
    ans += A[i]
if ans<0:
    ans1 = ans * -1
if ans>=0:
    ans1 = ans * -1
print(ans1)
