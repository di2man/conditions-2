try:

   user_select = int(input("Enter action:"))
   n1 = 70
   n2 = 7
   if user_select == "+":
      print("n1 + n2")
   elif user_select == "-":
          print("n1 - n2")
   elif user_select == "*":
       print("n1 * n2")
   elif user_select == "/":
    print("n1 / n2")
finally:
    print("end of count")
