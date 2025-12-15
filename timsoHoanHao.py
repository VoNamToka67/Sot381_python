n = int(input("Nhập số n: "))
tong = 0
for i in range(1, n):
    if n % i == 0:
        tong +=  i
if tong == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải là số hoàn hảo")