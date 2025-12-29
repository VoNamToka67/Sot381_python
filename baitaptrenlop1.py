n = int(input("Nhap so n:"))
x = int(input("Nhap so x:"))
tong = 0
tong1 = 1
for i in range (1, n+1):
    tong +=  (x)**0.5
    tong1 +=(x**i)/(i+1)
print (tong)
print (tong1)


    