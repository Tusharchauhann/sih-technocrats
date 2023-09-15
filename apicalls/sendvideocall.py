import requests

# Define the URL of your Flask API
api_url = 'http://localhost:5000/upload'  # Update with your API URL

# Path to the MP4 video file you want to upload
video_file_path = './my_video.mp4'  # Update with the actual file path

# Create a dictionary containing the file to be uploaded
files = {'video': ('video.mp4', open(video_file_path, 'rb'))}

try:
    # Send a POST request to the API endpoint
    response = requests.post(api_url, files=files)

    # Check the response from the API
    if response.status_code == 200:
        print('File uploaded successfully')
    elif response.status_code == 400:
        print('Invalid request or file format')
    else:
        print('An error occurred:', response.text)

except requests.exceptions.RequestException as e:
    print('An error occurred:', str(e))
