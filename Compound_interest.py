p,r,t=map(int,input().split())
x=p*(pow((1+r/100),t))
print("{0:.2f}".format(x))