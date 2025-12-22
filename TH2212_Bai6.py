n = int(input("Nhap so luong bai hat:"))
danhsachbaihat= []
for i in range(n):
    baihat = input(f"Bai hat thu {i+1} la:")
    danhsachbaihat.append(baihat)
for i in range(n):
    ten = danhsachbaihat[i]
    TEN = ten.upper()
    print(TEN)
print (danhsachbaihat)
    