import os
from pytube import YouTube
import streamlit as st


st.header(":blue[Fetch by Tarmica]")

screen = st.text_input("Enter YouTube Link")
download_button = st.button("Download")

options = ["Video", "Audio"]
choice = st.radio("Select download option:", options)


def download_video():
    yt = YouTube(screen)
    download_path = os.path.join(
        os.path.expanduser("~"), "Downloads", "Fetch by Tarmica"
    )
    yt.streams.filter(progressive=True, file_extension="mp4").order_by(
        "resolution"
    ).desc().first().download(output_path=download_path)
    st.write("Video downloaded into " + download_path)


def download_audio():
    yt = YouTube(screen)
    download_path = os.path.join(
        os.path.expanduser("~"), "Downloads", "Fetch by Tarmica"
    )
    yt.streams.filter(only_audio=True).first().download(output_path=download_path)
    st.write("Audio downloaded into " + download_path)


if download_button:
    if choice == "Video":
        download_video()
    else:
        download_audio()
