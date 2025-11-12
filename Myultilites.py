print("=" * 60)
print("CHƯƠNG TRÌNH TÍNH TIỀN ĐIỆN")
print("=" * 60)

# Bảng giá điện
gia_dien = {
    "1.1": {
        "ten": "Cấp điện áp từ 110 kV trở lên",
        "gio_binh_thuong": 1811,
        "gio_thap_diem": 1146,
        "gio_cao_diem": 3266
    },
    "1.2": {
        "ten": "Cấp điện áp từ 22 kV đến dưới 110 kV",
        "gio_binh_thuong": 1833,
        "gio_thap_diem": 1190,
        "gio_cao_diem": 3398
    },
    "1.3": {
        "ten": "Cấp điện áp từ 6 kV đến dưới 22 kV",
        "gio_binh_thuong": 1899,
        "gio_thap_diem": 1234,
        "gio_cao_diem": 3508
    },
    "1.4": {
        "ten": "Cấp điện áp dưới 6 kV",
        "gio_binh_thuong": 1987,
        "gio_thap_diem": 1300,
        "gio_cao_diem": 3640
    }
}

# Hiển thị menu chọn loại điện
print("\nChọn loại điện sử dụng:")
print("1.1 - Cấp điện áp từ 110 kV trở lên")
print("1.2 - Cấp điện áp từ 22 kV đến dưới 110 kV")
print("1.3 - Cấp điện áp từ 6 kV đến dưới 22 kV")
print("1.4 - Cấp điện áp dưới 6 kV")
print("-" * 60)

loai_dien = input("Nhập loại điện (1.1, 1.2, 1.3, 1.4): ")

if loai_dien not in gia_dien:
    print("Lỗi: Loại điện không hợp lệ!")
else:
    print(f"\nBạn đã chọn: {gia_dien[loai_dien]['ten']}")
    print("-" * 60)

    # Nhập số điện tiêu thụ theo từng khung giờ
    print("\nNhập số điện đã tiêu thụ (kWh):")

    so_dien_binh_thuong = float(input("a) Giờ bình thường: "))
    so_dien_thap_diem = float(input("b) Giờ thấp điểm: "))
    so_dien_cao_diem = float(input("c) Giờ cao điểm: "))

    # Tính tiền điện
    tien_binh_thuong = so_dien_binh_thuong * gia_dien[loai_dien]["gio_binh_thuong"]
    tien_thap_diem = so_dien_thap_diem * gia_dien[loai_dien]["gio_thap_diem"]
    tien_cao_diem = so_dien_cao_diem * gia_dien[loai_dien]["gio_cao_diem"]

    tong_tien = tien_binh_thuong + tien_thap_diem + tien_cao_diem
    tong_so_dien = so_dien_binh_thuong + so_dien_thap_diem + so_dien_cao_diem

    # Hiển thị kết quả
    print("\n" + "=" * 60)
    print("HÓA ĐƠN TIỀN ĐIỆN")
    print("=" * 60)
    print(f"Loại điện: {gia_dien[loai_dien]['ten']}")
    print("-" * 60)
    print(f"{'Khung giờ':<25} {'Số kWh':>12} {'Đơn giá':>10} {'Thành tiền':>12}")
    print("-" * 60)
    print(
        f"{'Giờ bình thường':<25} {so_dien_binh_thuong:>12.2f} {gia_dien[loai_dien]['gio_binh_thuong']:>10} {tien_binh_thuong:>12,.0f}")
    print(
        f"{'Giờ thấp điểm':<25} {so_dien_thap_diem:>12.2f} {gia_dien[loai_dien]['gio_thap_diem']:>10} {tien_thap_diem:>12,.0f}")
    print(
        f"{'Giờ cao điểm':<25} {so_dien_cao_diem:>12.2f} {gia_dien[loai_dien]['gio_cao_diem']:>10} {tien_cao_diem:>12,.0f}")
    print("-" * 60)
    print(f"{'TỔNG CỘNG':<25} {tong_so_dien:>12.2f} kWh {' ':>10} {tong_tien:>12,.0f} đồng")
    print("=" * 60)
    print(f"\nSố tiền phải thanh toán: {tong_tien:,.0f} đồng")
    print("=" * 60)