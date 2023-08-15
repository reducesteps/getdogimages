from flask import Flask, send_from_directory, render_template
import os
from download_dog_images import download_dog_image

app = Flask(__name__)

@app.route('/download')

def download_image():
    download_dog_image()
    return 'Image downloaded successfully'

@app.route('/view')

def view_images():
    images = os.listdir('dogpics')
    return render_template('gallery.html', images=images)

@app.route('/images/<filename>')

def send_image(filename):
    return send_from_directory('dogpics', filename)

if __name__ == '__main__':
    app.run(debug=True)
