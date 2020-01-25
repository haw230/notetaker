from flask import Flask, render_template, request
from notetaker.process import master_parser, get_image
import json

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/')
def start_home():
    return render_template('notetaker.html')

@app.route('/receiveData', methods=['GET', 'POST'])
def receive_data():
    data = json.loads(str(request.get_data(), 'utf-8'))['data']
    print(f'Receive Data: {data}')
    return master_parser(data)

@app.route('/receiveImage', methods=['GET', 'POST'])
def receive_image():
    print(request.get_data())
    data = json.loads(str(request.get_data(), 'utf-8'))['data']
    print(f'Receive Image: {data}')
    image_url = get_image(data)
    print(f'Received Image Url: {image_url}')
    return image_url


@app.route('/subtitles')
def start_subtitles():
    return render_template('subtitle.html')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['TESTING'] = True
    app.run(debug=True, host='0.0.0.0')