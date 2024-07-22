H = int(input())
D = 0
P = 0
while True:
    P += 2**D
    D += 1
    if H<P:
        print(D)
        break