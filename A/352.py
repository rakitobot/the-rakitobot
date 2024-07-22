

N,X,Y,Z = map(int,input().split())
load = [0]  * N
ans = [0]  * N
for i in range(N):
    load[i] = i +1
if X>Y:
    ans_start = load.index(X)
    ans_end = load.index(Y)
    
    for i in range(ans_end+1,ans_start+1):
        if i == Z:
            print("Yes")
            exit()
    print("No")
if X<Y:
    ans_start = load.index(X)
    ans_end = load.index(Y)
    
    for i in range(ans_start+1,ans_end+1):
        if i == Z:
            print("Yes")
            exit()
    print("No")
    



    
    
    
    
    
    
    
    
    
    
    
    # for i in range(ans_start+1):
        # ans[i] = i+1
# ans.reverse()
# print(ans)


