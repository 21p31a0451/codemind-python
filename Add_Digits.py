def digit_sum(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

# Prompt the user to enter a number
input_num = int(input())

output_num = digit_sum(input_num)
print( output_num)