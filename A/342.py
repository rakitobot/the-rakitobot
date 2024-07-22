S = list(input())
if S[0] != S[1]:
    if S[-1] == S[1]:
        print(1)
        exit()
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        # if S[i+1] != S[-1]:
            # print(len(S+1))
            # exit()
        if S[i+1] == S[-1]:
            print(i+2)
            exit()
        print(i+2)
        exit()
