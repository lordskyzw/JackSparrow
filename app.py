from flask import Flask, request, jsonify
import pytube  # Assuming you are using pytube for downloading

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    youtube_url = data.get('url')
    if not youtube_url:
        return jsonify({'error': 'No URL provided'}), 400

    # Your logic to download the video and get the download link
    # For now, let's assume you're getting a direct download link
    try:
        video = pytube.YouTube(youtube_url)
        video_stream = video.streams.filter(progressive=True, file_extension='mp4').first()
        download_link = video_stream.url  # Or any other way you handle downloads

        return jsonify({'downloadLink': download_link})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
