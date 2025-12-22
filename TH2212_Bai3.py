def soln(a,b,c):
    gtln = a
    if b > gtln:
        gtln = b
    if c > gtln:
        gtln = c
    return gtln
a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
c = int(input("Nhap so c:"))
nMax =soln(a,b,c)
print(nMax)
        

    