from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class VideoUpload(Resource):
    def post(self):
        try:
            # Check if the 'video' field is in the request
            if 'video' not in request.files:
                return {'message': 'No file part'}, 400

            video_file = request.files['video']

            # Check if a file was uploaded
            if video_file.filename == '':
                return {'message': 'No selected file'}, 400

            # Check if the file extension is valid (MP4)
            if video_file.filename.endswith('.mp4'):
                # Save the file to a desired location
                video_file.save('uploaded_videos/' + video_file.filename)

                return {'message': 'File uploaded successfully'}, 200
            else:
                return {'message': 'Invalid file format'}, 400
        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(VideoUpload, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
