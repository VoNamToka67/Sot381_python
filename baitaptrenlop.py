Toan = int(input("Nhap diem mon toan:"))
Ly = int(input("Nhap diem mon ly:"))
Hoa = int(input("Nhap diem mon hoa:"))
Tong = Toan + Ly + Hoa
if Tong >= 15 and Toan > 4 and Ly > 4 and Hoa > 4:
    print ("Pass")
    if Toan > 5 and Ly > 5 and Hoa > 5:
        print ("Hoc deu cac mon")
    else:
        print ("Hoc chua deu cac mon")
else:
    print ("Thi Hong")


    
