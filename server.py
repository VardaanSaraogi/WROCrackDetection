import os
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('upload_image')
def handle_image_upload(image_data):
    if image_data:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.png')
        with open(filename, 'wb') as f:
            f.write(image_data)
        emit('image_uploaded', 'Image uploaded successfully')

if __name__ == '__main__':
    socketio.run(app, debug=True)