def soLN_va_soNN(a,b,c):
    gtln = a
    if b > gtln:
        gtln = b
    if c > gtln:
        gtln = c
    gtnn = a
    if b < gtnn:
        gtnn = b
    if c < gtnn:
        gtnn = c
    return gtln,gtnn
a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
c = int(input("Nhap so c:"))
nMax,nMin =soLN_va_soNN(a,b,c)
print(f"Gia tri lon nhat la: {nMax}")
print(f"Gia tri nho nhat la:{nMin}")