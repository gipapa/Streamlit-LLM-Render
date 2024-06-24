import streamlit as st
from decouple import config
import openai, os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


response = False
prompt_tokens = 0
completion_tokes = 0
total_tokens_used = 0
cost_of_response = 0




st.header("Streamlit plus OpenAI ChatGPT/GPT3.5 turbo")

st.markdown("""---""")

question_input = st.text_input("Enter question/prompt! 輸入問題/提示！")
api_key_input = st.text_input("Enter Your OPENAI api key! 輸入你的OPENAI api key！")
rerun_button = st.button("Rerun 運行")

st.markdown("""---""")


#API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key_input


def make_request_backup(question_input: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{question_input}"},
        ]
    )
    return response

def make_request(question_input: str):    
    chat = ChatGroq(temperature=0.5, model="llama3-70b-8192", api_key='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')
    system = "You are a helpful assistant."
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    chain = prompt | chat
    return chain.invoke({"text": "Explain the importance of low latency for LLMs."}).content     
    





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
'''    
    st.write(response["choices"][0]["message"]["content"])

    prompt_tokens = response["usage"]["prompt_tokens"]
    completion_tokes = response["usage"]["completion_tokens"]
    total_tokens_used = response["usage"]["total_tokens"]

    cost_of_response = total_tokens_used * 0.000002
else:
    pass


with st.sidebar:
    st.title("Usage Stats:")
    st.markdown("""---""")
    st.write("Promt tokens used/提示token使用量:", prompt_tokens)
    st.write("Completion tokens used/Completion toekn使用量:", completion_tokes)
    st.write("Total tokens used/token使用總量:", total_tokens_used)
    st.write("Total cost of request/全部花費: ${:.8f}".format(cost_of_response))
'''