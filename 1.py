## 1.)Given an input string, print the string with the first and last letter removed if they were equal, or the original string if they were not.
inputStr = 's' 
lenght=len(inputStr)
if lenght==1:
   print(inputStr)
else:
   if inputStr[0]==inputStr[-1]:
      print(inputStr[1:-1])
   else:
      print(inputStr)

