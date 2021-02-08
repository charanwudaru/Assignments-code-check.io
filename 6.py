x = 0 
y = 0 
z = 0 

if (x==y==z):
   print("All")
elif (x!=y and y!=z):
   print("Distinct")
elif (x==y or x!=z):
   print("Two")
elif (y==z or y!=z):
   print("Two")
