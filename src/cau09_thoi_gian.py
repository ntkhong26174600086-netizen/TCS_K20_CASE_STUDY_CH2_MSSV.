from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
#phép toán thoi_luong = ket_thuc - bat_dau lấy mốc thời gian 15:05 trừ đi 13:15 cùng ngày 14/10/2026
#nên kết quả của phép trừ sẽ ra là 1:50:00 tương đương 1 giờ 50 phút

#GIẢI THÍCH SỰ KHÁC NHAU GIỮA DATETIME/STR/TIME/DELTA
# 1. KIỂU DATETIME (MỐC THỜI GIAN)
# - Bản chất: Là một đối tượng (object) đại diện cho một ĐIỂM THỜI GIAN cố định
# - Trong ví dụ: 'bat_dau' và 'ket_thuc' là datetime (ngày 14/10/2026 lúc 13:15 và 15:05)
# - Đặc điểm: Lưu trữ đầy đủ thông tin năm, tháng, ngày, giờ, phút, giây
# - Khả năng: Python hiểu được giá trị của nó nên có thể dùng để thực hiện phép trừ

# 2. KIỂU STR (CHUỖI KÝ TỰ / VĂN BẢN)
# - Bản chất: Chỉ là một CHUỖI CHỮ thuần túy, dùng để hiển thị cho con người đọc
# - Trong ví dụ: 'thoi_diem_text' là một chuỗi có dạng "2026-10-14 13:15:00"
# - Đặc điểm: Đối với Python, chuỗi này không khác gì một đoạn văn bản thông thường
# - Khả năng: KHÔNG THỂ thực hiện các phép toán cộng trừ thời gian với kiểu dữ liệu này

# 3. KIỂU TIMEDELTA (KHOẢNG THỜI GIAN)
# - Bản chất: Là kết quả của hiệu số, đại diện cho một KHOẢNG THỜI GIAN TRÔI QUA
# - Trong ví dụ: 'thoi_luong' là timedelta (kết quả sau khi lấy 'ket_thuc' trừ 'bat_dau')
# - Đặc điểm: Không gắn liền với ngày tháng cụ thể nào, chỉ lưu số ngày, số giây chênh lệch.
# - Khả năng: Định dạng hiển thị mặc định có dạng H:MM:SS (ví dụ trong bài là 1:50:00)
