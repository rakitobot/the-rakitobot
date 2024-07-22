N,T,P = map(int,input().split())
Li = list(map(int,input().split()))
count = 0 
ans = 0
count2 = 0
for i in range(N):
    if Li[i]>=T:
        count2 += 1
if count2>=P:
    print(0)
    exit()
while True:
    ans += 1
    for i in range(len(Li)):
        Li[i] += 1
    for i in range(N):
        if Li[i]>=T:
            count += 1  
        if count>=P:
            print(ans)
            exit()
    count = 0




# for i in range(N):
#     T[i] += 1 
#     ans += 1
#     if T[i] == P:
#         count += 1
#         if count == P:
#             print(ans)

    
