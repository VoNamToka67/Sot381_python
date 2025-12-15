while True:
    n = int(input("Nhập n (0 < n < 10): "))
    if 0 < n < 10:
        break
    else:
        print("n không hợp lệ, nhập lại!")
gt = 1
for i in range(1, n + 1):
    gt *= i
print(f"{n}! =", gt)