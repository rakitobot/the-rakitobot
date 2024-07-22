N = int(input())
once = [0] * N*2
G = 0
for i in range(N):
    once[i+G] = 1
    G += 1 
once.append(1)   
print(*once,sep='')
