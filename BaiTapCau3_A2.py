n = int(input("Nhap so luong phan tu :"))
ds = []
chan = 0
for i in range (n):
    so = int(input(f"So thu {i} la :"))
    ds.append(so)
for x in range (0,len(ds),2):
    chan +=ds[x]        
print (ds)
print (chan)
    
              

