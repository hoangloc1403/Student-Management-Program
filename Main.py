from libs.xu_ly_du_lieu import *
danh_sach_hoc_sinh = [
]
_path ="files/ket_qua.csv"
file_path ="files/hoc_sinh.csv"
doc_du_lieu_tu_file(file_path, danh_sach_hoc_sinh)
while True:
    print("\nCHƯƠNG TRÌNH QUẢN LÝ HỌC SINH")
    print("1: Thêm học sinh")
    print("2: Danh sách học sinh")
    print("3: Tra cứu học sinh ")
    print("4: Xóa học sinh ")
    print("5: Tính điểm trung bình và xếp loại ")
    print("6: Lưu kết quả ")
    try:
        choice = int(input("Chọn chứ năng cần thực hiện: "))
        if not (1 <= choice <=6):
            raise ValueError("Vui lòng nhập lựa chọn từ 1 đến 6!")
        if choice  == 1:
            them_hoc_sinh(danh_sach_hoc_sinh)
        elif choice == 2:
            in_danh_sach_hoc_sinh(danh_sach_hoc_sinh)
        elif choice == 3:
            tra_cuu_hoc_sinh(danh_sach_hoc_sinh)
        elif choice == 4:
            mahs = input("Cho biết Mã HS: ")
            result = xoa_hoc_sinh(danh_sach_hoc_sinh,mahs)
            if result == 1:
                print("Đã xóa")
            else:
                print("Không tìm thấy học sinh với mã học sinh đã nhập.")
        elif choice == 5:
            tinh_dtb_xep_loai(danh_sach_hoc_sinh)
        elif choice == 6:
            ket_qua(danh_sach_hoc_sinh,_path)
    except ValueError as err:
        print("Lỗi:",err)
        continue
    select_choice = input("Ban co muon tiep tuc chương trình (1:TT): ")
    if select_choice != "1":  
        break