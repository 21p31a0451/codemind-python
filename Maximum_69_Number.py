n=int(input())
tmp=str(n)
a=''
for i in tmp:
    a=a+i
z=tmp.find('6')
if z==-1:
    print(n)
elif z==0:
    n+=3000
    print(n)
elif z==1:
    n+=300
    print(n)
elif z==2:
    n+=30
    print(n)
elif z==3:
    n+=3
    print(n)
    