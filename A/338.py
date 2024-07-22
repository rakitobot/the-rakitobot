S = input()
A = S.upper()
count = 0
if S[0] == A[0]:
    A = S.lower()
    count += 1
    for i in range(len(S)-1):
        if S[i+1] == A[i+1]:
            count += 1
if count == len(S):
    print("Yes")
    exit()            

print("No")