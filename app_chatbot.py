import os
import streamlit as st 
from langchain_groq import ChatGroq 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.chains.combine_documents import create_stuff_documents_chain 
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
print(groq_api_key)
google_api_key=os.getenv("GOOGLE_API_KEY")

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

st.title("Gemma model QnA bot")

llm=ChatGroq(groq_api_key=groq_api_key, model_name='gemma-7b-it')
st.write(llm)

prompt_template=ChatPromptTemplate.from_template(
    """
    Answer the question only based on given context.
    Please provide the response based on the question
    <context>
    {context}
    <contezt>
    Question:{input}
    """
)


def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader=PyPDFDirectoryLoader("./papers") # Data Ingesion
        st.session_state.docs=st.session_state.loader.load() # data loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
        
        

prompt1=st.text_input("Enter your Question")

if st.button("Creating a vector store."):
    vector_embedding()
    st.write("Vecot store DB is ready")
    
import time

if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt_template)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    
    start=time.process_time()
    response=retrieval_chain.invoke({'input':prompt1})
    
    st.write(response['answer'])
    
    # with a streamlit expander
    with st.expander("Document similarity search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("------------------------------------")
            
    