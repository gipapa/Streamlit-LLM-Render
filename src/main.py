import naive_chatbot
import chatbot_search_memory

import streamlit as st
import os

PAGES = {
    '🤖原生的無狀態對話機器人': naive_chatbot,
    '🤖可紀錄對話歷史,上網查詢相關內容': chatbot_search_memory
}

MODELS = [
    'gemma2-9b-it',
    'gemma-7b-it',
    'llama3-70b-8192',
    'llama3-8b-8192',
    'mixtral-8x7b-32768',    
]

#bot selector
st.set_page_config(page_title="Gipapa Chatbot POC", page_icon="🦜")
st.sidebar.title('Chatbot Garden')
selection = st.sidebar.radio('choose and go', list(PAGES.keys()))

#model selector
st.sidebar.title('Models')
model_selection = st.sidebar.radio('models from qroq', MODELS)

GROQ_SETTING = {
    'API_KEY' :os.getenv("GROQ-token"),
    'MODEL' : MODELS[model_selection],
    'TEMPERATURE':'0.5'
}


page = PAGES[selection]
page.app(GROQ_SETTING)
