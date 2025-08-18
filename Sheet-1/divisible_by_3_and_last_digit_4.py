num = int(input("Enter a number: "))
last_digit = abs(num) % 10
divisible_by_3 = num % 3 == 0

if divisible_by_3 and last_digit == 4:
    print(f"{num} is divisible by 3 and ends with 4")
else:
    print(f"{num} does not meet both conditions")
    if not divisible_by_3:
        print(f"{num} is not divisible by 3")
    if last_digit != 4:
        print(f"Last digit is {last_digit}, not 4")
