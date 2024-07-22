ans = 0
N = int(input())
S = [0] * 100
for i in range(N):
    S[i] = input()
for i in range(N):
    if S[i] == "Takahashi":
        ans = ans + 1
        
print(ans)