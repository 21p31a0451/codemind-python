n=int(input())
add=0
pro=1
while n:
    rem=n%10
    n=n//10
    add=add+rem
    pro=pro*rem

if add==pro:
    print("Spy Number")
else:
    print("Not Spy Number")