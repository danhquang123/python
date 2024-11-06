
# tiến trình 1
print("         Phần mềm tính toán điểm trung bình ")

# tiến trình 2
ten  = input  ("Nhập tên của bạn : ")
toan = input  ("Nhập điểm Toán: ")
van  = input  ("Nhập điểm Văn: ")
anh  = input  ("Nhập điểm Anh: ")

# tiến trình 3
toan = float(toan)
van  = float(van)
anh  = float(anh)

# tiến trình 4
diem_trung_binh = (toan + van + anh) / 3

# tiến trình 5 

print(f"Điểm trung bình cộng  ba môn của học sinh {ten} là: {diem_trung_binh:.2f}")
