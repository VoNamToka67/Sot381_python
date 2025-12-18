n = int(input("Nhập số n từ bàn phím:"))
ds = []
for i in range (n):
    so = int(input(f"Nhập phần tử thứ {i+1} = "))
    ds.append(so)
print(ds)
tong = sum(ds)
print("Tổng của danh sách trên là:",tong)