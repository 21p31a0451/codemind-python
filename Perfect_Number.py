def is_perfect_number(num):
    if num <= 0:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    return divisors_sum == num

# Prompt the user to enter a number
input_num = int(input())

if is_perfect_number(input_num):
    print(True)
else:
    print(False)
