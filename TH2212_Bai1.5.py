while True:
    a = float(input("Nhap canh a:"))
    if a > 0:
        break
while True:
    b = float(input("Nhap canh b:"))
    if b > 0:
        break
while True:
    c = float(input("Nhap canh c:"))
    if c > 0:
        break
cv = (a+b+c)/2
dt = (cv*(cv-a)*(cv-b)*(cv-c))**0.5
print (f"Dien tich la: {dt}")
print (f"Chu vi la: {cv}")