S = list(input())
S[-1] = str(int(S[-1]) + 1)
print(*S,sep='')
