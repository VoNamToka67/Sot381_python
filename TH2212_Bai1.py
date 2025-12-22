while True:
    m = float(input("Nhap chieu dai:"))
    if m >= 0:
        break
    else:
        print("So ko hop le")
while True:
    n = float(input("Nhap chieu rong:"))
    if n <=100:
        break
    else:
        print("so ko hop le")
P = (m+n)*2
S = m*n
print (f"Dien tich hcn la :{S:.2f}")
print (f"Chu vi hcn la :{P:.2f}")   