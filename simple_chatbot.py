import streamlit as st
import time  # Để mô phỏng thời gian phản hồi

st.title("Chatbot Hỏi Đáp Đơn Giản")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Bạn muốn hỏi gì?"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Logic chatbot đơn giản ---
    if "thời tiết" in prompt.lower():
        chatbot_response = "Thời tiết hôm nay ở Hải Dương khá đẹp, trời nắng nhẹ."
    elif "giờ" in prompt.lower():
        current_time = time.strftime("%H:%M:%S")
        chatbot_response = f"Bây giờ là {current_time} tại Hải Dương."
    elif "chào" in prompt.lower():
        chatbot_response = "Xin chào! Rất vui được trò chuyện với bạn."
    else:
        chatbot_response = "Tôi xin lỗi, tôi chưa hiểu câu hỏi này. Bạn có thể hỏi lại không?"

    # Mô phỏng thời gian phản hồi của chatbot
    time.sleep(1)

    st.session_state["messages"].append({"role": "assistant", "content": chatbot_response})
    with st.chat_message("assistant"):
        st.markdown(chatbot_response)
        
    # Panel lịch sử ở sidebar
with st.sidebar:
    st.subheader("Lịch Sử Trò Chuyện")
    for i, msg in enumerate(st.session_state["messages"]):
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
        if i < len(st.session_state["messages"]) - 1:
            st.divider()