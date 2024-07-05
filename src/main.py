import naive_chatbot
import chatbot_search_memory

import streamlit as st

GROQ_SETTING = {
    'API_KEY' :os.getenv("GROQ-token"),
    'MODEL' :"llama3-70b-8192",
    'TEMPERATURE':'0.5'
}

PAGES = {
    '🤖原生的無狀態對話機器人': naive_chatbot,
    '🤖可紀錄對話歷史,上網查詢相關內容': chatbot_search_memory
}

st.set_page_config(page_title="Gipapa Chatbot POC", page_icon="🦜")
st.sidebar.title('Chatbot Garden')
selection = st.sidebar.radio('choose and go', list(PAGES.keys()))
page = PAGES[selection]
page.app(GROQ_SETTING)
