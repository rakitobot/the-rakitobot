N,L,R = map(int,input().split())
ans = None
A = [0] * N
for i in range(N):
    A[i] = i+1
ans = A[L-1:R] 
# 0:L-2:ans:R:N-1
for i in range(L-1):
    print(A[i],end=" ")
for i in range(R-L+1):
    print(ans[-i-1],end=" ")
for i in range(R,N):
    print(A[i],end=" ")



