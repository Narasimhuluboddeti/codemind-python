n=int(input())
m=list(map(int,input().split()))
c=0
for i in range(1,len(m)-1):
    if m[i]%2==1 and m[i-1]%2==1 and m[i+1]%2==1:
        c+=1
print(c)