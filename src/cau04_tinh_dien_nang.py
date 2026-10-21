cong_suat_w = 250
so_phut = 60
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh - Kiểu: {type(dien_nang_kwh)}")
print(f"Chi phí điện: {chi_phi} VNĐ - Kiểu: {type(chi_phi)}")
#Điện năng: 250 * 90 / 60 / 1000 = 22500 / 60000 = 0.375 kWh.
#Chi phí: 0.375* 3000 = 1125.0 VNĐ.
# Tính toán lại với 60 phút 
#Điện năng: $250* 60 / 60 / 1000 = 250 / 1000 = 0.25 kWh
#Chi phí: 0.25 * 3000 = 750.0 VNĐ 
#So sánh kết quả giữa hai trường hợp
#Khi thời gian giảm từ 90 phút xuống 60 phút ,lượng điện năng tiêu thụ cũng giảm tương ứng từ 0.375 kWh xuống 0.25 kWh
# Chi phí tiền điện giảm từ $1125$ VNĐ xuống $750$ VNĐ