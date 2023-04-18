import base64
import streamlit as st
import pytube
import uuid
import os

st.set_page_config(page_title="Tarmic's YouTube Downloader", page_icon=":arrow_down:")

st.title("Tarmic's YouTube Downloader")

url = st.text_input("Enter the YouTube video URL below", "")
if url:
    try:
        video = pytube.YouTube(url)

        st.write("Title:", video.title)
        st.write("Length:", video.length, "seconds")

        with st.spinner("Downloading..."):
            stream = video.streams.get_highest_resolution()
            file_id = str(uuid.uuid4())
            stream.download(filename=file_id)
        st.success("Download Successful!")

        file_path = os.path.join(os.getcwd(), f"{file_id}.mp4")
        st.write("Download link:")
        st.markdown(
            f'<a href="data:file/mp4;base64,{base64.b64encode(open(file_path, "rb").read()).decode()}" download="{video.title}.mp4">Generate link</a>',
            unsafe_allow_html=True,
        )

    except pytube.exceptions.PytubeError as e:
        st.error(str(e))
