try:
   user_select = int(input("Enter menu number:"))
   match user_select:
      case 1: print("Monday")
      case 2: print("Tuesday")
      case 3: print("Wednesday")
      case 4: print("Thursday")
      case 5: print("Friday")
      case 6: print("Saturday")
      case 7: print("Sunday")
except Exeptation as e: print(f"Error: {e}")
