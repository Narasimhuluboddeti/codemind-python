P,T,R=map(int,input().split())
R=R/100
a=P*(1+(R*T))
i=a-P
print(int(i))
