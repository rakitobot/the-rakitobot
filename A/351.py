A = list(map(int,input().split()))
B = list(map(int,input().split()))
score_A = 0 
score_B = 0 
for i in range(9):
    score_A +=  A[i]
for i in range(8):
    score_B += B[i]
print(score_A - score_B +1)  
