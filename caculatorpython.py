a= float(int(input("Nhập số:")))
b= float(int(input("Nhập số:")))
c= input("các dấu (+,-,*,/,):")
if c == "+" :
  print (a+b)
if c == "-" :
  print (a-b)
if c == "*":
  print (a*b)
if c== "/" and b>0:
  print (a/b)
else:
  print ("Phép tính lỗi")

