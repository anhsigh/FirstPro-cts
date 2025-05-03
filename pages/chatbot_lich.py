"""Module chứa logic chính cho chatbot lịch."""

import streamlit as st
from modules import exporter

# import datetime
# import pandas as pd
# import io

if "lich_da_luu" not in st.session_state:
    st.session_state["lich_da_luu"] = []

with st.form(key="form_them_lich"):
    mo_ta = st.text_input("Mô tả sự kiện:")
    ngay_bat_dau = st.date_input("Ngày bắt đầu:")
    thoi_gian_bat_dau = st.time_input("Thời gian bắt đầu:")
    ngay_ket_thuc = st.date_input("Ngày kết thúc:")
    thoi_gian_ket_thuc = st.time_input("Thời gian kết thúc:")
    nut_them = st.form_submit_button("Thêm lịch")

if nut_them:
    if mo_ta:
        su_kien = {
            "mô tả": mo_ta,
            "ngày_bat_dau": ngay_bat_dau,
            "thời_gian_bat_dau": thoi_gian_bat_dau,
            "ngày_ket_thuc": ngay_ket_thuc,
            "thời_gian_ket_thuc": thoi_gian_ket_thuc,
        }
        st.session_state["lich_da_luu"].append(su_kien)
        st.success(f"Đã thêm sự kiện '{mo_ta}' vào lịch.")
    else:
        st.warning("Vui lòng nhập mô tả cho sự kiện.")

if st.session_state["lich_da_luu"]:
    st.subheader("Lịch đã lưu:")
    st.dataframe(st.session_state["lich_da_luu"])

st.subheader("Lưu lịch vào file CSV:")
if st.button("Lưu vào CSV"):
    ten_cac_truong_lich = [
        "mô tả",
        "ngày_bat_dau",
        "thời_gian_bat_dau",
        "ngày_ket_thuc",
        "thời_gian_ket_thuc",
    ]
    thanh_cong, thong_bao = exporter.luu_du_lieu_csv(
        st.session_state["lich_da_luu"],
        ten_file="lich.csv",
        ten_cac_truong=ten_cac_truong_lich,
    )
    if thanh_cong:
        st.success(thong_bao)
        # Đoạn code để tải file CSV sau khi lưu thành công
        with open("lich.csv", "r", encoding="utf-8") as f:
            csv_data = f.read()

        st.download_button(
            label="Tải xuống file CSV",
            data=csv_data,
            file_name="lich.csv",
            mime="text/csv",
        )
    else:
        st.error(thong_bao)
