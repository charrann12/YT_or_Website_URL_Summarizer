import validators, streamlit as st 
from langchain_classic.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
import os

## Streamlit APP 

st.set_page_config(page_title = "LangChain: Summarize Text from YT or Website")
st.title("LangChain: Summarize Text from YT or Website")
st.subheader("Summarize URL")


## Get the GROQ API key and url(YT or website) to be summarized 

with st.sidebar:
    groq_api_key = st.text_input("Groq API key", value = "", type = "password")

generic_url = st.text_input("URL", label_visibility = "collapsed")


prompt_template = """ 
    Provide summary of the following content in 300 words:
    Content:{text}
"""

prompt = PromptTemplate(template = prompt_template, input_variables = ['text'])

if st.button("Summmarize"):

    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid url. It can be a YT video url or website url")
    
    else:
        try:

            llm = ChatGroq(model = "llama-3.3-70b-versatile", groq_api_key = groq_api_key)

            with st.spinner("Waiting"):
                ## Loading the website or YT video data

                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                        generic_url,
                        add_video_info = False
                    )
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify  = False,
                        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    )
                docs = loader.load()

                ##    Chain for summarization 
                chain = load_summarize_chain(llm, chain_type = "stuff", prompt = prompt)
                output_summary = chain.invoke(docs)                            

                st.success(output_summary['output_text'])
        
        except Exception as e:
            st.exception(e)



    



