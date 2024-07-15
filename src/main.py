import naive_chatbot
import chatbot_search_memory
import streamlit as st
import os
from streamlit_card import card

PAGES = {
    'chatbot_search_memory': {
        'title': 'RAG bot',
        'description': '🤖可紀錄對話歷史,上網查詢相關內容',
        'module': chatbot_search_memory
    },
    'naive_chatbot': {
        'title': 'bot',
        'description': '🤖原生的無狀態對話機器人',
        'module': naive_chatbot
    },
}

MODELS = {
    'llama3-70b-8192': 'Llama 3 70B',
    'llama3-8b-8192': 'Llama 3 8B',
    'gemma2-9b-it': 'Gemma 2 9B',
    'gemma-7b-it': 'Gemma 7B',    
    'mixtral-8x7b-32768': 'Mixtral 8x7B',    
}

def initialize_session_state():
    if 'page_selection' not in st.session_state:
        st.session_state.page_selection = None
    if 'model_selection' not in st.session_state:
        st.session_state.model_selection = list(MODELS.keys())[0]
    if 'temperature' not in st.session_state:
        st.session_state.temperature = 0.5
    update_groq_setting()

def sidebar_selections():
    st.sidebar.title('Setting')
    
    if st.session_state.page_selection:
        model_selection = st.sidebar.selectbox('Language model:', 
                                               list(MODELS.keys()),
                                               index=list(MODELS.keys()).index(st.session_state.model_selection),
                                               format_func=lambda x: MODELS[x],
                                               key='model_selectbox')        
        
        temperature = st.sidebar.text_input('Temperature:', 
                                            value=str(st.session_state.temperature),
                                            key='temperature_input')
        
        # Convert temperature to float and validate
        try:
            temperature = float(temperature)
            if temperature < 0 or temperature > 1:
                st.sidebar.warning('Temperature should be between 0 and 1')
                temperature = st.session_state.temperature
        except ValueError:
            st.sidebar.warning('Please enter a valid number for temperature')
            temperature = st.session_state.temperature
        
        if (model_selection != st.session_state.model_selection or 
            temperature != st.session_state.temperature):
            st.session_state.model_selection = model_selection
            st.session_state.temperature = temperature
            update_groq_setting()
    
    return st.session_state.model_selection, st.session_state.temperature

def update_groq_setting():
    st.session_state.groq_setting = {
        'API_KEY': os.getenv("GROQ-token"),
        'MODEL': st.session_state.model_selection,
        'TEMPERATURE': str(st.session_state.temperature)
    }

def display_dashboard():
    st.title('Chatbot Garden Dashboard')
    
    col1, col2 = st.columns(2)
    
    for idx, (key, page_info) in enumerate(PAGES.items()):
        with col1 if idx % 2 == 0 else col2:
            if card(title=page_info['title'], text=page_info['description'], key=f"card_{idx}"):
                st.session_state.page_selection = key
                st.experimental_rerun()

def main():
    st.set_page_config(page_title="Gipapa Chatbot POC", page_icon="🦜", layout="wide")
    
    initialize_session_state()
    model_selection, temperature = sidebar_selections()
    
    if st.session_state.page_selection is None:
        display_dashboard()
    else:
        if st.button("Back to Dashboard"):
            st.session_state.page_selection = None
            st.experimental_rerun()
        
        page = PAGES[st.session_state.page_selection]['module']
        page.app()

if __name__ == "__main__":
    main()