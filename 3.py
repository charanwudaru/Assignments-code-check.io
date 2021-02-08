inputStr = 'a1' 

if(inputStr[0] == 'a' or inputStr[0] == 'c' or inputStr[0] == 'e' ):
   if(inputStr[1] == '1' or inputStr[1] == '3' or inputStr[1] == '5' or inputStr[1] == '7'):
      print("Black")
   else:
      print("White")

else:
   if(inputStr[1] == '1' or inputStr[1] == '3' or inputStr[1] == '5' or inputStr[1] == '7'):
      print("White")
   else:
      print("Black")
