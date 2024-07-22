A,B,C = map(int,input().split())
D = list(map(int,input().split()))
for i in range(A):
    print(D[i],end=" ")
    if i == B-1:
        print(C,end=" ")


