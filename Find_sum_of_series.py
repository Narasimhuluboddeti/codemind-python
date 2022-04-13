n=int(input())
s=0
c=0
for i in range(1,n+1):
    s=1/i
    c+=s
print("%0.2f"%c)