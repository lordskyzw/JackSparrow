from pytube import YouTube
import streamlit as st

st.header(":blue[Tarmica & The Carribean Pirates]")

# Allow user to select whether to download video or audio file
file_type = st.radio("Select file type", ("Video", "Audio"))

# Get YouTube link from user
screen = st.text_input("Enter YouTube link")

# Download file when user clicks the download button
if st.button("Download"):
    if file_type == "Video":
        # Download video file
        video = YouTube(screen)
        stream = video.streams.get_highest_resolution()
        stream.download()
        st.write("Video file downloaded")
    elif file_type == "Audio":
        # Download audio file
        video = YouTube(screen)
        stream = video.streams.get_audio_only()
        stream.download()
        st.write("Audio file downloaded")
