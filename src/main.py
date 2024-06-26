import streamlit as st
from decouple import config
import openai, os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


response = False

st.header("Streamlit plus groq")

st.markdown("""---""")

question_input = st.text_input("Enter question/prompt! 輸入問題/提示！")
rerun_button = st.button("run")

st.markdown("""---""")

API_KEY = os.getenv("GROQ-token")

def make_request(question_input: str):    
    chat = ChatGroq(temperature=0.5, model="llama3-70b-8192", api_key=API_KEY)
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