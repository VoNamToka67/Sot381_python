n = int(input("Nhập số lượng số n từ bàn phím:"))
ds = []
for i in range (n):
    so = int(input(f"Số thứ {i} là :"))
    ds.append(so)
sochan = [x for x in ds if x%2==0]
sole = [y for y in ds if y %2==1]
print(ds)
print(sochan)
print(sole)
