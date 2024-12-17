import streamlit as st  
import time 
from src.utils import save_uploadedfile,remove_uploadedfile 

st.set_page_config(page_icon='💬',page_title='ChatWithPdf')
st.title("💬 Chatbot")
st.caption("🚀 A chatbot powered by Siddharth")

with st.sidebar:
    global pdf 
    qroq_api_key = st.text_input('Enter your API key',type="password")
    pdf = st.file_uploader('upload pdf file') 
    if pdf:
        st.warning('I am Processing Pdf!')
        path = save_uploadedfile(pdf)
        time.sleep(2)
        st.success(f'PDF save successfully in {path}')
        time.sleep(3)
        remove_uploadedfile()
        st.success(f'PDF remove successfully in {path}')




if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": " I am ready for answering.How can I help you?"}]

if pdf:
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    if prompt:=st.chat_input('Enter your question'):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt) 
        with st.spinner('Wait for AI response...'):
            time.sleep(3)
            response ='i am siddharth ' 
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
            




