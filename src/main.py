import naive_chatbot
import chatbot_search_memory

import streamlit as st
PAGES = {
    'naive_chatbot': naive_chatbot,
    'chatbot_search_memory': chatbot_search_memory
}

st.set_page_config(page_title="Gipapa Chatbot POC", page_icon="🦜")
st.sidebar.title('Chatbot Garden')
selection = st.sidebar.radio('choose and go', list(PAGES.keys()))
page = PAGES[selection]
page.app()