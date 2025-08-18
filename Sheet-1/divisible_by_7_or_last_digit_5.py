num = int(input("Enter a number: "))
last_digit = abs(num) % 10
divisible_by_7 = num % 7 == 0
if divisible_by_7 or last_digit == 5:
    print(f"{num} meets at least one condition:")
    if divisible_by_7:
        print(f"  - {num} is divisible by 7")
    if last_digit == 5:
        print(f"  - Last digit is 5")
else:
    print(f"{num} does not meet either condition")
    print(f"  - Not divisible by 7")
    print(f"  - Last digit is {last_digit}, not 5")
