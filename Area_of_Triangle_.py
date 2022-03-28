a,b,c=map(int,input().split())
s=((a+b+c)/2)
n=(s*((s-a)*(s-b)*(s-c)))
print("%0.2f"%(n**0.5))