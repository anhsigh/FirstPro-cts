import streamlit as st
import time

st.title("Trợ Lý Ghi Nhớ")

# Khởi tạo state cho tin nhắn và thông tin đã nhớ
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "remembered_info" not in st.session_state:
    st.session_state["remembered_info"] = {}

# Panel lịch sử ở sidebar
with st.sidebar:
    st.subheader("Lịch Sử Trò Chuyện")
    for i, msg in enumerate(st.session_state["messages"]):
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
        if i < len(st.session_state["messages"]) - 1:
            st.divider()

# Xử lý tin nhắn của người dùng
if prompt := st.chat_input("Bạn muốn nói gì?"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Logic chatbot với khả năng ghi nhớ ---
    response = ""
    if "tên tôi là" in prompt.lower():
        name = prompt.lower().split("tên tôi là")[-1].strip()
        st.session_state["remembered_info"]["name"] = name
        response = f"Chào {name}! Tôi sẽ nhớ tên bạn."
    elif "tôi sống ở" in prompt.lower():
        location = prompt.lower().split("tôi sống ở")[-1].strip()
        st.session_state["remembered_info"]["location"] = location
        response = f"Tôi sẽ nhớ bạn sống ở {location}."
    elif "bạn biết gì về tôi" in prompt.lower():
        info = []
        if "name" in st.session_state["remembered_info"]:
            info.append(f"Tên bạn là {st.session_state['remembered_info']['name']}.")
        if "location" in st.session_state["remembered_info"]:
            info.append(f"Bạn sống ở {st.session_state['remembered_info']['location']}.")
        if info:
            response = "Tôi biết những điều sau về bạn:\n" + "\n".join(info)
        else:
            response = "Tôi chưa biết gì về bạn cả."
    else:
        response = "Tôi xin lỗi, tôi chưa hiểu. Bạn có thể cho tôi biết thêm thông tin về bạn không?"

    time.sleep(1)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)