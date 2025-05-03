import streamlit as st

st.title("Chatbot Đơn Giản")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Nhập tin nhắn...")

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Đây là nơi bạn tích hợp logic chatbot thực tế ---
    # Ví dụ đơn giản: mô phỏng phản hồi
    chatbot_response = f"Chào bạn! Bạn đã nói: '{prompt}'"

    st.session_state["messages"].append(
        {"role": "assistant", "content": chatbot_response}
    )
    with st.chat_message("assistant"):
        st.markdown(chatbot_response)
