import csv

def doc_du_lieu_tu_file(file_path,danh_sach_hoc_sinh):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            danh_sach_hoc_sinh.append(row)
    return danh_sach_hoc_sinh

def kiem_tra_ton_tai(mahs,danh_sach_hoc_sinh):
    for hoc_sinh in danh_sach_hoc_sinh:
        if hoc_sinh['mahs'] == mahs:
            return True  
    return False
def kiem_tra_nhap_diem(mon):
    while True:
        try:
            diem = float(input(f"Điểm {mon}: "))
            if 0 <= diem <= 10:
                return diem
            else:
                print(f"Điểm {mon} phải nằm trong khoảng từ 0 đến 10.")
        except ValueError:
            print("Vui lòng nhập số.")
def them_hoc_sinh(danh_sach_hoc_sinh):
    while True:
        hoc_sinh_dict = {}
        mahs = input("Mã học sinh: ")
        if kiem_tra_ton_tai(mahs,danh_sach_hoc_sinh):
            print("=== Mã học sinh đã tồn tại ===\n")
            continue 
        hoten = input("Họ tên HS: ")
        diemmon1 = kiem_tra_nhap_diem("môn 1")
        diemmon2 = kiem_tra_nhap_diem("môn 2")      
        diemmon3 = kiem_tra_nhap_diem("môn 3") 
        hoc_sinh_dict = {'mahs':mahs,'hoten':hoten, 'diemmon1':diemmon1,'diemmon2':diemmon2,'diemmon3':diemmon3}
        danh_sach_hoc_sinh.append(hoc_sinh_dict)
        select_choice = input("Ban co muon tiep tuc (1:TT): ")
        if select_choice != "1":  
            break
def in_danh_sach_hoc_sinh(danh_sach_hoc_sinh):
    if not danh_sach_hoc_sinh:
        print("Không có học sinh nào.")
        return
    print(f"{'Ma HS':8}{'Họ ten':20}{'Mon 1':>8}{'Mon 2':>8}{'Mon 3':>8}")
    for i in danh_sach_hoc_sinh:
        print(f"{i['mahs']:8}{i['hoten']:20}{i['diemmon1']:8}{i['diemmon2']:8}{i['diemmon3']:8}")
def tra_cuu_hoc_sinh(danh_sach_hoc_sinh):
    mahs = input("Cho biết Mã HS: ")
    found = False
    for i in danh_sach_hoc_sinh:
        if i['mahs'] == mahs:
            print(f"{'Ma HS':8}{'Họ ten':20}{'Mon 1':>8}{'Mon 2':>8}{'Mon 3':>8}")
            print(f"{i['mahs']:8}{i['hoten']:20}{i['diemmon1']:8}{i['diemmon2']:8}{i['diemmon3']:8}")
            found = True
            break
    if not found:
        print("Không tìm thấy học sinh với mã học sinh đã nhập.")
def xoa_hoc_sinh(danh_sach_hoc_sinh,mahs):
    for hoc_sinh in danh_sach_hoc_sinh:
        if hoc_sinh['mahs'] == mahs:
            danh_sach_hoc_sinh.remove(hoc_sinh)
            return 1
    return 0
def tinh_dtb_xep_loai(danh_sach_hoc_sinh):
    if not danh_sach_hoc_sinh:
        print("Không có học sinh nào trong danh sách.")
        return
    for hoc_sinh in danh_sach_hoc_sinh:
        diemmon1 = float(hoc_sinh['diemmon1'])
        diemmon2 = float(hoc_sinh['diemmon2'])
        diemmon3 = float(hoc_sinh['diemmon3'])
        diem_trung_binh = (diemmon1 + diemmon2 + diemmon3) / 3
        hoc_sinh['DTB'] = diem_trung_binh
        if 0<= diem_trung_binh <5:
            hoc_sinh['XepLoai'] = 'Kém'
        elif 5<= diem_trung_binh <= 6.5:
            hoc_sinh['XepLoai'] = 'Trung Bình'
        elif 6.5<diem_trung_binh <8:
            hoc_sinh['XepLoai'] = 'Khá'
        elif 8 <= diem_trung_binh <9:
            hoc_sinh['XepLoai'] = 'Giỏi'
        elif diem_trung_binh >=9:
            hoc_sinh['XepLoai'] = 'Xuất sắc'
    print(f"{'Ma HS':8}{'Họ ten':20}{'Mon 1':>8}{'Mon 2':>8}{'Mon 3':>8}{'DTB':>5}{'Xep Loai':>18}")
    for hoc_sinh in danh_sach_hoc_sinh:
        print(f"{hoc_sinh['mahs']:8}{hoc_sinh['hoten']:20}{hoc_sinh['diemmon1']:8}{hoc_sinh['diemmon2']:8}{hoc_sinh['diemmon3']:8}{hoc_sinh['DTB']:>5.2f}{hoc_sinh['XepLoai']:>18}")
def ket_qua(danh_sach_hoc_sinh,_path):
    if not danh_sach_hoc_sinh:
        print("Không có học sinh nào để lưu.")
        return
    field_names = ['mahs', 'hoten', 'diemmon1', 'diemmon2', 'diemmon3', 'DTB', 'XepLoai']
    with open(_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(danh_sach_hoc_sinh)
    print(f"Đã lưu")