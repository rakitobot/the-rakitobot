N = int(input())
ans = [0] * N 
for i in  range(N):
    ans[i] = i+1
for i in range(N):
    if ans[i]%3 == 0:
        print("x",end="")
    else:
        print("o",end="")

