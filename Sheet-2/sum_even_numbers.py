a = int(input("enter a no. "))
sum = 0
for i in range(1, a+1):
    if i % 2 == 0:
        sum += i
print(sum)
