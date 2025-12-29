def so_nguyen_to (n):
    result = True
    if n < 2:
        result = False
    elif n == 2:
        result = True
    elif n % 2 == 0:
        result = False
    for i in range (3, int(n**0.5) + 1 , 2):
        if n % 1 ==0:
            result = False
    return result
n = int(input("Nhap so luong phan tu :"))
ds = []
songuyento = 0
for i in range (n):
    so = int(input(f"So thu {i} la :"))
    ds.append(so)
for i in ds:
    if so_nguyen_to(i)==True:
        print(i,end=' ');songuyento+=1
print()
print (songuyento)
        




    


