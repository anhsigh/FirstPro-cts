import streamlit as st

st.title("Chào mừng đến với Ứng dụng của tôi!")
st.write("Đây là trang chủ của ứng dụng.")
st.write(
    "Bạn có thể sử dụng các trang ở sidebar bên trái để khám phá các tính năng."  # noqa: E501
)

st.sidebar.title("Điều hướng")
st.sidebar.write("Chọn một trang để tiếp tục:")

# Streamlit sẽ tự động phát hiện các file .py trong thư mục 'pages/'
# và hiển thị chúng trong sidebar. Tên hiển thị sẽ dựa trên tên file.
# Ví dụ: chatbot_lich.py sẽ hiển thị là "Chatbot Lich" hoặc "Chatbot_lich".

st.sidebar.info(
    "Sử dụng sidebar để chuyển đổi giữa trang chủ và trang quản lý lịch."
)
