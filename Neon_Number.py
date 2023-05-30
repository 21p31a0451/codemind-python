
n=int(input())
sq=pow(n,2)
tot=0
for i in str(sq):
    tot=tot+int(i)
if tot==n:
    print("Neon Number")
else:
    print("Not Neon Number")
