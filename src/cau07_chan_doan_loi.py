ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Lỗi 1:Lỗi cú pháp (SyntaxError) do thiếu dấu ngoặc đóng ')' ở dòng print cuối cùng.
# Lỗi 2 :Lỗi kiểu dữ liệu (TypeError) do 'cong_suat_w' là chuỗi (str) từ hàm input() nhưng lại thực hiện phép toán số học.
# Lỗi 3 :Lỗi tên biến (NameError) do gọi sai tên biến 'dien_nang' thay vì 'dien_nang_kwh' trong hàm print.