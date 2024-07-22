A,B = list(map(int,input().split()))
ans = A + B 
for i in range(9):
    if ans != i:
        print(i)
        exit()