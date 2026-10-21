tong_phut = 135
cong_suat_w = 250
so_gio = tong_phut //60
so_phut_con_lai = tong_phut % 60
print(f"{tong_phut} phút tương đương với {so_gio} giờ {so_phut_con_lai} phút.")
su_dung_lau = tong_phut >60
print(f"su_dung_lau = {su_dung_lau}")
du_lieu_hop_le = (cong_suat_w>0) and (tong_phut>0)
print(f"du_lieu_hop_le = {du_lieu_hop_le}")
bt_1= 100+20*3
bt_2= (100+20)*3
print(f"Biểu thức 1: 100 + 20 * 3= {bt_1}")
#Theo quy tắc toán học (nhân chia trước, cộng trừ sau), Python sẽ thực hiện phép nhân 20 * 3 = 60 trước, sau đó mới cộng với 100. Kết quả là 160
print(f"Biểu thức 2: (100 + 20) * 3= {bt_2}")
#Theo quy tắc toán học phải nhân trong () trước ,Python tính trong ngoặc trước 100 + 20 = 120, sau đó nhân với 3. Kết quả là 360.