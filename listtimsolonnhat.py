n = int(input("Nhập số n bất kỳ:"))
ds = []
for i in range(n):
    so = int(input(f"Số thứ {i+1} là:"))
    ds.append(so)
solonnhat = max(ds)
print (solonnhat)