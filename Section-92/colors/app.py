import os
from flask import Flask, render_template, request
from PIL import Image
from collections import Counter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def get_dominant_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.resize((150, 150))  # Resize to speed up processing
    image = image.convert('RGB')
    pixels = list(image.getdata())
    counter = Counter(pixels)
    most_common = counter.most_common(num_colors)
    return most_common

@app.route('/', methods=['GET', 'POST'])
def index():
    colors = []
    uploaded_file = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            uploaded_file = file.filename
            colors = get_dominant_colors(filepath)
    return render_template('index.html', colors=colors, uploaded_file=uploaded_file)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
