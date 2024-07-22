B = input()
for i in range(3):
    if "R" == B[i]:
        A = i 
for i in range(3):
    if "M" == B[i]:
        C = i 
if A<=C:
    print("Yes")
else:
    print("No")


