R,G,B = map(int,input().split())
C = input()
if C == "Blue":
    if R<=G:
        print(R)
    else:
        print(G)
if C == "Red":
    if B<=G:
        print(B)
    else:
        print(G)
if C == "Green":
    if R<=B:
        print(R)
    else:
        print(B)
        
