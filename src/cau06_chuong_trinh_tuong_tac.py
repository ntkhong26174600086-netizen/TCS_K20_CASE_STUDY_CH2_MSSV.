#mã phiên, mã máy, công suất, số
#phút sử dụng và đơn giá. Sau đó tính điện năng và chi phí.

ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất (W): "))
so_phut = int(input("Nhập số phút sử dụng: "))
don_gia = float(input("Nhập đơn giá (VNĐ/kWh): "))

dien_nang_kwh = (cong_suat_w * so_phut) /60/1000
chi_phi = dien_nang_kwh * don_gia
print(f"Mã phiên: {ma_phien}")
print(f"Mã máy: {ma_may}")
print(f"Điện năng tiêu thụ: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí sử dụng: {chi_phi:.1f} VNĐ")