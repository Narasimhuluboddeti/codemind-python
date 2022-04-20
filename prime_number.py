def prime(n):
    if n==1 and n==0:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
    return True

n=int(input())
if prime(n)==True:
    print("prime")
else:
    print("not a prime")