toan = (float(input("Nhập điêm TB môn Toán:")))
anh = (float(input("Nhập điêm TB môn Anh:")))
van = (float(input("Nhập điêm TB môn Văn:")))
sinh = (float(input("Nhập điêm TB môn Sinh:")))
su = (float(input("Nhập điêm TB môn Sử:")))
tin = (float(input("Nhập điêm TB môn Tin:")))
hoa = (float(input("Nhập điêm TB môn Hóa:")))
ly = (float(input("Nhập điêm TB môn Lý:")))
DiemTB= (toan + anh + van + sinh + su + hoa + ly + tin) / 8
if DiemTB >= 9.0:
    xeploai= "Học sinh Xuất sắc"
elif DiemTB >= 8.0:
    xeploai= "Học Sinh Giỏi"
elif DiemTB >= 6.5:
    xeploai= "Học Sinh Khá"
elif DiemTB >= 5.0:
    xeploai= "Học sinh Trung Bình"
else:
    xeploai= "Học sinh Yếu"
print ("Điểm của bạn là:",DiemTB)
print ("Xếp hạng của bạn là:",xeploai)
