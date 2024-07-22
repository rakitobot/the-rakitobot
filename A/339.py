S = input()
ans = S.rfind('.')
A = [0] * (len(S)-ans-1)
for i in range(len(S)-ans-1):
    A[i] = S[ans+i+1]
print(*A,sep='')


