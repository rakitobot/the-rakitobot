S = list(input())
count = 0
for i in range(len(S)-1):
    if S[i] == "|":
        for j in range(100):
            S.pop(i)
            if S[i] == "|":
                S.pop(i)
                print(*S,sep='')
                exit()
print(*S,sep='')