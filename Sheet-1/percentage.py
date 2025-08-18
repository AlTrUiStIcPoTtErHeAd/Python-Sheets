#Accept the percentage from the user and display the groade according to criteria. 
percent=int(input("Enter your Percentage:"))
if percent>=90:
   print("Grade O")
elif percent>=80:
   print("Grade A")
elif percent>=70:
  print("Grade B")
elif percent>=60:
  print("Grade C")
elif percent>=50:
  print("Grade D")
else:
  print("Grade F")
