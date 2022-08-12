m,n = map(int,input().split())
if 1<=m<=n<=16:
    s = n*m
    print(s//2)
else:
    print('restricted')