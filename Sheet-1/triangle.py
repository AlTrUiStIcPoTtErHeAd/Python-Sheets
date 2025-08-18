# You are given 3 integers angles of a triangle. Tell whther the triangle is valid or not.
a1=int(input("Enter first integer angle"))
a2=int(input("Enter second integer angle"))
a3=int(input("Enter third integer angle"))
if a1+a2+a3==180 and a1>0 and a2>0 and a3>0 and a1<180 and a2<180 and a3<180:
   print("The triangle is valid")
else:
   print("The triangle is not valid")


