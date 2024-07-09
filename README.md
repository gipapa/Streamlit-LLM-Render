# RAG service in Render
Streamlit-groq-langchain-Render: 使用各種套件來快速建置Web app於平台Render

demo url: https://web-p174.onrender.com/

demo url (in CHT OA): https://safeweb.secure365.hinet.net/https://web-p174.onrender.com/

 - forked from
    - joeychrys/streamlit-chatGPT/ (streamlit+chatgpt)
    - pyfbsdk59/Streamlit-ChatGPT3.5-Render (streamlit+chatgpt+render)
 - 🌐render可以取代heroku, 免費快速建立網頁服務: https://dashboard.render.com/
   - Start Command要改為streamlit run src/main.py來啟動
   - 未付費的話，服務一段時間沒存取會關閉，下次連線需要大量時間重啟，所以可以使用以下服務來定期存取 https://console.cron-job.org/dashboard
 - 🦜langchain: 整體LLM APP的agent框架，用來實現RAG與串接各種接口
 - ✨groq可以免費申請API，內含數個可高速存取的模型可以使用: https://groq.com/ 
 - 🦆DuckDuckGo: 用以私密搜尋
