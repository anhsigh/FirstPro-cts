import csv
import datetime


def luu_lich_csv(danh_sach_lich, ten_file="lich.csv"):
    """
    Lưu danh sách các sự kiện lịch vào một file CSV.

    Args:
        danh_sach_lich (list): Danh sách các dictionary, mỗi dictionary đại diện cho một sự kiện lịch.
        ten_file (str, optional): Tên của file CSV để lưu. Mặc định là 'lich.csv'.
    """  # noqa: E501
    try:
        with open(ten_file, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["mô tả", "ngày", "thời gian"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for su_kien in danh_sach_lich:
                # Đảm bảo rằng các đối tượng datetime được định dạng đúng khi ghi vào CSV # noqa: E501
                su_kien_ghi = {
                    "mô tả": su_kien["mô tả"],
                    "ngày": (
                        su_kien["ngày"].isoformat()
                        if isinstance(su_kien["ngày"], datetime.date)
                        else su_kien["ngày"]
                    ),
                    "thời gian": (
                        su_kien["thời gian"].isoformat()
                        if isinstance(su_kien["thời gian"], datetime.time)
                        else su_kien["thời gian"]
                    ),
                }
                writer.writerow(su_kien_ghi)
        return True, f"Đã lưu lịch vào file {ten_file}"
    except Exception as e:
        return False, f"Lỗi khi lưu vào file CSV: {e}"


if __name__ == "__main__":
    # Ví dụ sử dụng (có thể bỏ qua khi import module)
    du_lieu_mau = [
        {
            "mô tả": "Họp nhóm dự án",
            "ngày": datetime.date(2025, 5, 4),
            "thời gian": datetime.time(9, 0),
        },
        {"mô tả": "Nộp báo cáo", "ngày": "2025-05-05", "thời gian": "17:00"},
    ]
    thanh_cong, thong_bao = luu_lich_csv(du_lieu_mau, "mau_lich.csv")
    if thanh_cong:
        print(thong_bao)
    else:
        print(thong_bao)
