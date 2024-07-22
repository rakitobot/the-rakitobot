S1 = input()
S = list(S1)
count = 0
if S[0] != "<" or S[-1] != ">":
    print("No")
    exit()
    
for i in range(1,len(S)-1):
        if S[i] != "=":
            print("No")
            exit()
        count += 1
if count == len(S)-2:
    print("Yes")
    exit()

           