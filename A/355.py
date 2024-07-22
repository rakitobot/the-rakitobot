A,B = map(int,input().split())
if A == B:
    print(-1)
    exit()
for i in range(3):
    if A != i+1 and B != i+1:
        print(i+1)