point = [0, 0] 
x = float(point[0])
y = float(point[1])


if x < 0:
   if y > 0:
      print("Second")
   elif (point[1] == 0):
      print("X-axis")
   else:
      print("Third")
elif (point[0] == 0 and point[1] == 0):
   print("Origin")

elif (point[0] == 0):
   print("Y-axis")
   
if x > 0:
   if y > 0:
      print("First")
   else:
      print("Fourth")
