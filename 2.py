inputStr = 'a1' 
last = [ 'a8', 'h8','a1', 'h1']
margin = ['b1','c1','d1','e1','f1','g1'','b8','c8','d8','e8','f8','g8','h2','h3','h4','h5','h6','h7','a2','a3','a4','a5','a6','a7]

if(inputStr in last):
   print("Corner")
elif(inputStr in margin):
   print("Border")
else:
   print("Inside")
