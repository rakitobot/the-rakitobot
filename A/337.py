N = int(input())
score1 = 0
score2 = 0
for i in range(N):
    X,Y = map(int,input().split())
    score1 = score1 + X
    score2 = score2 + Y
if score1>score2:
    print("Takahashi")
    exit()
if score1 == score2:
    print("Draw")
    exit()

print("Aoki")
