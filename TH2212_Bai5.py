def tinhS(n):
    ts = 0
    for i in range (1, n+1):
        ts += i
    ms = 0
    for i in range (2, 2*n+2, 2):
        ms += i
    S = ts/ms
    return S
n = int(input("Nhap so n:"))
ketqua = tinhS(n)
print (ketqua)

    
    