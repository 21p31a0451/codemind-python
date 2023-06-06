def print_table(x,y):
    for i in range(1, y+1):
        if i % 2 == 0:
            continue
        result = x * i
        print(f"{x} x {i} = {result}")

x,y= map(int, input().split())

print_table(x,y)
