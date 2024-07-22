M,D = map(int,input().split())
y,m,d = map(int,input().split())
count = 0
if D<=d:
    d = 1
    count += 1
else:
    d += 1
if count == 1:
    m += 1
if M < m:
    m = 1
    count += 1
if count == 2:
    y += 1
print(y,m,d)

