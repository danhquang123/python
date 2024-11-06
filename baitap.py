
# Danh sách lưu trữ thông tin sinh viên


def add_student(msv_dong):
    
    name = input("Nhập tên sinh viên: ")
    age = int(input("Nhập tuổi sinh viên: "))
    nganh = input("Chuyên ngành: ")
    msv_tmp="sv"+str(msv_dong);
    new_student = {"Msv": msv_tmp, "Ten": name, "Tuoi": age, "nganh": nganh}
    students.append(new_student)
    print("Đã thêm thành công!")

def display_students():
    if not students:
        print("Không có sinh viên nào.")
    else:
        print("Danh sách sinh viên:")
        for student in students:
            print("__________________________________________________________________________________________________________________")
            print(f"Mã sinh viên: {student['Msv']}, Tên: {student['Ten']}, Tuổi: {student['Tuoi']}, Chuyên Ngành: {student['nganh']}")
            print("__________________________________________________________________________________________________________________")
def update_student():
    print("Danh sách sinh viên có thể sửa")
    display_students()
    student_id = input("Nhập mã sinh viên cần sửa: ")
    for student in students:
        
        if student["Msv"] == student_id:
            print("Thông tin hiện tại:", student)
            student["Ten"] = input("Nhập tên mới: ")
            student["Tuoi"] = int(input("Nhập tuổi mới: "))
            student["nganh"] = input("Nhập chuyên ngành mới: ")
            print("Thông tin sinh viên đã cập nhật thành công!")
            
            return()
    print("Không tìm thấy sinh viên.")

def delete_student():
    print("Danh sách sinh viên có thể xoá")
    display_students()
    student_id = input("Nhập mã sinh viên cần xoá: ")
    for student in students:
        if student["Msv"] == student_id:
            students.remove(student)
            print("Sinh viên đã xoá thành công!")
            return
    






students = [
    {"Msv": "sv1", "Ten": "Nguyễn Danh Quang", "Tuoi": 20, "nganh": "CNTT"},
    {"Msv": "sv2", "Ten": "Bùi Văn Tâm", "Tuoi": 21, "nganh": "CNTT"}
]
msv_dong=2

while True:
    print("\n_________ Quản lý sinh viên __________")
    print("1. Thêm sinh viên")
    print("2. Hiển thị sinh viên")
    print("3. Sửa thông tin sinh viên")
    print("4. Xoá sinh viên")
    print("5. Thoát chương trình")
    print("______________________________________")
    luachon = input("Nhập lựa chọn của bạn: ")

    if  luachon == '1':
        tmp=int(input("Số lượng học sinh muốn thêm"))
        
        for i in range(tmp):
            print("Hãy nhập học sinh thứ ",i+1)
            msv_dong+=1
            add_student(msv_dong)
        display_students();
        print("Danh sách sinh viên khi được cập nhật")
    elif  luachon == '2':
        display_students()
    elif  luachon == '3':
        
        
        update_student()
        display_students();
        print("Danh sách sinh viên khi được cập nhật")
        
    elif  luachon == '4':
        
        
        delete_student()
            
        display_students();
        print("Danh sách sinh viên khi được cập nhật")
    elif  luachon == '5':
        print("Chương trình đã tắt")
        break
    else:
        print("Lựa chọn không đúng, vui lòng nhập lại!")







