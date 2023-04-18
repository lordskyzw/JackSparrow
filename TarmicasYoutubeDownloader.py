import streamlit as st
import pytube
import base64
import os
import uuid

# Set the download folder path
DOWNLOAD_PATH = os.path.expanduser("~") + "/Downloads/"


# Generate unique filename using uuid
def generate_filename(video):
    return f"{video.title}-{str(uuid.uuid4())[:8]}.mp4"


# Define a function to download the video
def download_video(url):
    # Get the video details
    st.write("Getting video details...")
    video = pytube.YouTube(url)

    # Get the highest resolution stream
    st.write("Getting highest resolution stream...")
    stream = video.streams.get_highest_resolution()

    # Download the video
    st.write("Downloading video...")
    file_path = DOWNLOAD_PATH + generate_filename(video)
    stream.download(output_path=DOWNLOAD_PATH, filename=generate_filename(video))

    # Generate the download link
    st.markdown(
        f'<a href="data:file/mp4;base64,{base64.b64encode(open(file_path, "rb").read()).decode()}" download="{generate_filename(video)}">Generate link to download {video.title}</a>',
        unsafe_allow_html=True,
    )


# Set the app title
st.set_page_config(page_title="Tarmicas Youtube Downloader")

# Display the app title
st.title("Tarmicas Youtube Downloader")

# Get the video URL from the user
url = st.text_input("Enter the URL of the video you want to download:")

# Download the video when the user clicks the "Download" button
if st.button("Download"):
    download_video(url)
