import csv
import datetime
from typing import List, Dict, Union


def luu_du_lieu_csv(
    danh_sach_du_lieu: List[
        Dict[str, Union[str, datetime.date, datetime.time]]
    ],  # noqa: E501
    ten_file: str = "du_lieu.csv",
    ten_cac_truong: List[str] = None,
):
    """
    Lưu danh sách các dictionary dữ liệu vào một file CSV.

    Args:
        danh_sach_du_lieu (list): Danh sách các dictionary, mỗi dictionary đại diện cho một hàng dữ liệu.  # noqa: E501
        ten_file (str, optional): Tên của file CSV để lưu. Mặc định là 'du_lieu.csv'.
        ten_cac_truong (list, optional): Danh sách các tên trường (keys của dictionary)  # noqa: E501
                                         để ghi vào file CSV theo thứ tự. Nếu None, sẽ sử dụng  # noqa: E501
                                         các keys từ dictionary đầu tiên.  # noqa: E501
    """
    try:
        if not danh_sach_du_lieu:
            return True, f"Không có dữ liệu để lưu vào file {ten_file}"

        if ten_cac_truong is None:
            ten_cac_truong = list(danh_sach_du_lieu[0].keys())

        with open(ten_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=ten_cac_truong)
            writer.writeheader()
            for du_lieu in danh_sach_du_lieu:
                row = {}
                for truong in ten_cac_truong:
                    value = du_lieu.get(truong)
                    if isinstance(value, (datetime.date, datetime.time)):
                        row[truong] = value.isoformat()
                    else:
                        row[truong] = value
                writer.writerow(row)
        return True, f"Đã lưu dữ liệu vào file {ten_file}"
    except Exception as e:
        return False, f"Lỗi khi lưu vào file CSV: {e}"


if __name__ == "__main__":
    # Ví dụ sử dụng
    du_lieu_lich = [
        {
            "mô tả": "Họp nhóm dự án",
            "ngày_bat_dau": datetime.date(2025, 5, 4),
            "thời_gian_bat_dau": datetime.time(9, 0),
            "ngày_ket_thuc": datetime.date(2025, 5, 4),
            "thời_gian_ket_thuc": datetime.time(10, 0),
        },
        {
            "tiêu đề": "Nộp báo cáo",
            "ngày край": "2025-05-05",
            "giờ край": "17:00",
            "trạng thái": "Hoàn thành",
        },
    ]

    # Lưu dữ liệu lịch với các trường cụ thể
    thanh_cong_lich, thong_bao_lich = luu_du_lieu_csv(
        du_lieu_lich[:1],  # Chỉ lấy sự kiện lịch đầu tiên
        ten_file="lich_chung.csv",
        ten_cac_truong=[
            "mô tả",
            "ngày_bat_dau",
            "thời_gian_bat_dau",
            "ngày_ket_thuc",
            "thời_gian_ket_thuc",
        ],  # noqa: E501
    )
    print(
        f"Lưu lịch: Thành công={thanh_cong_lich}, Thông báo={thong_bao_lich}"
    )

    # Lưu dữ liệu khác với các trường khác
    thanh_cong_khac, thong_bao_khac = luu_du_lieu_csv(
        du_lieu_lich[1:],  # Chỉ lấy sự kiện thứ hai
        ten_file="du_lieu_khac.csv",
        ten_cac_truong=[
            "tiêu đề",
            "ngày край",
            "giờ край",
            "trạng thái",
        ],  # noqa: E501
    )
    print(
        f"Lưu dữ liệu khác: Thành công={thanh_cong_khac}, Thông báo={thong_bao_khac}"  # noqa: E501
    )

    # Lưu tất cả dữ liệu, để hàm tự động lấy tên trường từ dictionary đầu tiên
    thanh_cong_tat_ca, thong_bao_tat_ca = luu_du_lieu_csv(
        du_lieu_lich, ten_file="tat_ca_du_lieu.csv"
    )  # noqa: E501
    print(
        f"Lưu tất cả: Thành công={thanh_cong_tat_ca}, Thông báo={thong_bao_tat_ca}"  # noqa: E501
    )
