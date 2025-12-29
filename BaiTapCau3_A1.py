n = int(input("Nhập số lượng số n từ bàn phím:"))
chan = 0
le = 0
ds = []
for i in range (n):
    so = int(input(f"Số thứ {i} là :"))
    ds.append(so)
for x in ds:
    if x %2==0:
        chan +=1
    else:
        le +=1
print (ds)
print ("Số lượng số chẵn là:",chan)
print ("Số lượng số lẻ là:", le)