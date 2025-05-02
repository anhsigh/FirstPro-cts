import streamlit as st
import datetime

if 'lich_da_luu' not in st.session_state:
    st.session_state['lich_da_luu'] = []

with st.form(key='form_them_lich'):
    mo_ta = st.text_input("Mô tả sự kiện:")
    ngay = st.date_input("Ngày:")
    thoi_gian = st.time_input("Thời gian:")
    nut_them = st.form_submit_button("Thêm lịch")

if nut_them:
    if mo_ta:
        su_kien = {
            'mô tả': mo_ta,
            'ngày': ngay,
            'thời gian': thoi_gian
        }
        st.session_state['lich_da_luu'].append(su_kien)
        st.success(f"Đã thêm sự kiện '{mo_ta}' vào lịch.")
    else:
        st.warning("Vui lòng nhập mô tả cho sự kiện.")

if st.session_state['lich_da_luu']:
    st.subheader("Lịch đã lưu:")
    st.dataframe(st.session_state['lich_da_luu'])