def sn(a,b):
    def sd(n):
        for d in str(n):
            if d=='0' or n%int(d)>0:
                return False
        return True
    out=[]
    for n in range(a,b+1):
        if sd(n):
            out.append(n)
    return out
a=int(input())
b=int(input())
print(*sn(a,b))   