import streamlit as st

# -------- PAGE CONFIG (like website settings) --------
st.set_page_config(
    page_title="My Chatbot",
    page_icon="💬",
    layout="centered"
)

# -------- SIDEBAR (like ChatGPT left panel) --------
with st.sidebar:
    st.title("💬 My Chatbot")
    if st.button("🆕 New Chat"):
        st.session_state.messages = []
    st.write("Made with Streamlit")

# -------- MAIN TITLE --------
st.title("Chat with my Bot 🤖")

# -------- CHAT HISTORY STORAGE --------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------- DISPLAY OLD MESSAGES --------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------- USER INPUT BOX --------
user_input = st.chat_input("Type your message here...")

if user_input:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # -------- BOT RESPONSE (simple logic) --------
    if "hi" in user_input.lower():
        bot_reply = "Hello! How can I help you today?"
    elif "your name" in user_input.lower():
        bot_reply = "I am your Streamlit chatbot 😊"
    else:
        bot_reply = "You said: " + user_input

    # Save bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.write(bot_reply)
