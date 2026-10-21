ma_may = input("Nhập mã máy: ")
cong_suat= input("Nhập công suất W: ")
so_phut= input("Nhập số phút sử dụng: ")
don_gia= input("Nhập đơn giá điện/kWh: ")
print(f"Kiểu của ma_may: {type(ma_may)}")
print(f"Kiểu của cong_suat: {type(cong_suat)}")
print(f"Kiểu của so_phut: {type(so_phut)}")
print(f"Kiểu của don_gia: {type(don_gia)}")
cong_suat_w = float(cong_suat)  # Chuyển sang float
so_phut = int(so_phut)          # Chuyển sang int
don_gia_kwh = float(don_gia)    # Chuyển sang float

print(f"Sau khi chuyển - Công suất ({type(cong_suat_w)}): {cong_suat_w}")
print(f"Sau khi chuyển - Số phút ({type(so_phut)}): {so_phut}")
print(f"Sau khi chuyển - Đơn giá ({type(don_gia_kwh)}): {don_gia_kwh}")
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(f"Mã máy: {ma_may}")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh (Kiểu: {type(dien_nang_kwh)})")
print(f"Chi phí điện: {chi_phi} VNĐ (Kiểu: {type(chi_phi)})")