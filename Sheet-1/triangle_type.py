a = int(input("Enter 1st Angle "))
b = int(input("Enter 2nd Angle "))
c = int(input("Enter 3rd Angle "))

if a + b + c != 180:
    print("Invalid triangle")
else:
    if a == 90 or b == 90 or c == 90:
        print("Right triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse triangle")
    else:
        print("Acute triangle")
