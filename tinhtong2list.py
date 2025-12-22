n1 = int(input("Số lượng danh sách 1:"))
ds1 =[]
for i in range (1,n1+1):
    so1 = int(input(f"Số thứ {i} là:"))
    ds1.append(so1)
n2 = int(input("Số lượng danh sách 2:"))
ds2 =[]
for i in range (1,n2+1):
    so2 = int(input(f"Số thứ {i} là:"))
    ds2.append(so2)
tong2list = sum(ds1) + sum(ds2)
print (ds1)
print (ds2)
print (tong2list)