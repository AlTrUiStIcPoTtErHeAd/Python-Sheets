# Write a program to input three numbers and find the minimum number among them.
a1= int(input("Enter the first number: "))
a2= int(input("Enter the second number: "))
a3= int(input("Enter the third number: "))
if a1 < a2 and a1 < a3:
    print("The minimum number is", a1)
elif a2 < a1 :
  print("The minimum number is", a2)
else:
  print("The minimum number is", a3)

