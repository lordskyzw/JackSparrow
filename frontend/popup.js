document.getElementById('downloadButton').addEventListener('click', function() {
  var youtubeUrl = document.getElementById('urlInput').value;
  if (youtubeUrl) {
    fetch('http://127.0.0.1:5000/download', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url: youtubeUrl })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('status').innerText = 'Download link: ' + data.downloadLink;
    })
    .catch(error => {
      console.error('Error:', error);
      document.getElementById('status').innerText = 'Error occurred';
    });
  } else {
    document.getElementById('status').innerText = 'Please enter a valid URL';
  }
});
