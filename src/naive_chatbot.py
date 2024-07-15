import streamlit as st
from decouple import config
import openai, os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

def app():

    API_KEY = st.session_state.groq_setting['API_KEY']
    MODEL = st.session_state.groq_setting['MODEL']
    TEMPERATURE= st.session_state.groq_setting['TEMPERATURE']

    response = False
    
    st.title('naive chatbot')
    st.write(f"✨groq({MODEL})")


    st.markdown("""---""")

    question_input = st.text_input("Enter question/prompt! 輸入問題/提示！")
    rerun_button = st.button("run")

    st.markdown("""---""")

    

    def make_request(question_input: str):    
        chat = ChatGroq(temperature=TEMPERATURE, model=MODEL, api_key=API_KEY, streaming=True)
        system = "You are a helpful assistant."
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        chain = prompt | chat
        return chain.invoke({"text": question_input}).content     
        

    if question_input:
        response = make_request(question_input)
    else:
        pass

    if rerun_button:
        response = make_request(question_input)
    else:
        pass

    if response:
        st.write("Response:")
        st.write(response)
