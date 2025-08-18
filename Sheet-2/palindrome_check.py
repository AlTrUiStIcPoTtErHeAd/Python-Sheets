a = int(input("enter a no:"))
original = a
reverse = 0
while a > 0:
    reverse = reverse * 10 + a % 10
    a //= 10
if original == reverse:
    print("Yes")
else:
    print("No")
