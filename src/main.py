import naive_chatbot
import chatbot_search_memory
import streamlit as st
import os

PAGES = {
    '🤖可紀錄對話歷史,上網查詢相關內容': chatbot_search_memory,
    '🤖原生的無狀態對話機器人': naive_chatbot,    
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
        st.session_state.page_selection = list(PAGES.keys())[0]
    if 'model_selection' not in st.session_state:
        st.session_state.model_selection = list(MODELS.keys())[0]
    if 'temperature' not in st.session_state:
        st.session_state.temperature = 0.5

def sidebar_selections():
    st.sidebar.title('Chatbot Garden')
    page_selection = st.sidebar.selectbox('Choose a chatbot:', 
                                          list(PAGES.keys()),
                                          index=list(PAGES.keys()).index(st.session_state.page_selection),
                                          key='page_selectbox')
    st.sidebar.markdown("""---""")
    st.sidebar.title('Setting')
    st.sidebar.markdown("""---""")
    st.sidebar.title('Models')
    model_selection = st.sidebar.selectbox('Choose a model:', 
                                           list(MODELS.keys()),
                                           index=list(MODELS.keys()).index(st.session_state.model_selection),
                                           format_func=lambda x: MODELS[x],
                                           key='model_selectbox')
    
    st.sidebar.title('Temperature')
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
    
    st.session_state.page_selection = page_selection
    st.session_state.model_selection = model_selection
    st.session_state.temperature = temperature
    
    return page_selection, model_selection, temperature

def main():
    st.set_page_config(page_title="Gipapa Chatbot POC", page_icon="🦜")
    
    initialize_session_state()
    page_selection, model_selection, temperature = sidebar_selections()
    
    GROQ_SETTING = {
        'API_KEY': os.getenv("GROQ-token"),
        'MODEL': model_selection,
        'TEMPERATURE': str(temperature)
    }
    
    page = PAGES[page_selection]
    page.app(GROQ_SETTING)

if __name__ == "__main__":
    main()
