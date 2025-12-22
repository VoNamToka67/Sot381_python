a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
c = int(input("Nhap so c:"))
ds = [a,b,c]
for i in ds:
    gtln = a
    if b > gtln:
        gtln = b
    if c > gtln:
        gtln = c
for i in ds:
    gtnn = a
    if b < gtnn:
        gtnn = b
    if c < gtnn:
        gtnn = c
print (ds)
print (f"Gia tri lon nhat la :{gtln}")
print (f"Gia tri nho nhat la :{gtnn}")
    

