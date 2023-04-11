from pytube import YouTube
import streamlit as st


st.header(":blue[Fetch by Tarmica]")

screen = st.text_input("Enter YouTube Link and click download")

download_button  = st.button(label="download")



def downloadd():
    YouTube(screen).streams.first().download(output_path=r'C:\Users\tarim\Downloads')
    st.write("downloading into C:\Users\tarim\Downloads")
    
if download_button:
    downloadd()

