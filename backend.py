from flask import Flask, render_template, request
from notetaker.process import master_parser, get_image
import json
import requests

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/')
def start_home():
    return render_template('notetaker.html')

@app.route('/receiveData', methods=['GET', 'POST'])
def receive_data():
    data = json.loads(str(request.get_data(), 'utf-8'))['data']
    print(f'Receive Data: {data}')
<<<<<<< Updated upstream
    return master_parser(data)
=======
    parsed_data = master_parser(data)
    print(parsed_data)
    return parsed_data

@app.route('/receiveLang', methods=['GET', 'POST'])
def receive_lang():
    data = json.loads(str(request.get_data(), 'utf-8'))['data']
    lang = json.loads(str(request.get_data(), 'utf-8'))['lang']
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'MIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQCay7guBjLBmgh6\niIOCkmSNuy5JJtKclE/SIF3LloMqaKwt37XUcaRaiNk3LYuiyJUuxL9inGZKPzAV\nN15zYTtZdRET6Nzh4XuIHkHOOHRr3h/rHdOzn3Zdqnu/O1zpTY7JoK5672J9+YI4\n9xbTQQlg3gbD3ypEJPRArPRfjVMhsntLxAxQzUodtLWF34VOkfOIxtg4TEwyozZ0\ntMnXmoq9/Unpn/uFR8FFR45lOcOIxwo2OycjeRFhwCWalqFfKcpMoL8NL1RywyyD\nSo4EnjchnDxjHoTl5EkV1LZFJrFc+dsOcA15YunjuEmZf27mwGa1kc4ZbeMuAmDV\n/v6fCllpAgMBAAECgf4RFVjsuDrkZmI1TWLbFytkI5gaKqn+qqL+lC0N2yCKdUl6\nsHqyGtva68cVn5NkX1NTNyQM2uS7XcJ1QlEF1n7ExXdkczPnH3SQXNQvYxGYK7lI\nqtDPZzIe8FCFpYjPXGcxhDrMPaKkvAO6XD363a07d9rZxAvHiBCq5bStBr7mQjAZ\nl0BSmavz6/VK8AWsnbyO+NZ4yMFeVA5kFOrI858kIOfHt2ZkA1cvnsp/MMrYzwRZ\nM3juDbBbFwx56VPvxcyzqKtJzAclVxkK1bZIPrHc0AnkXo+HLGMvVR4OzfWpEo06\nmzyIULcCC/WvMnQP/4B47JrxG4MeNZYv0SR//wKBgQDS+HSeyZpJSQGl7CC1B7ou\nIsElWLHwSXA0+1TclQlzUo5YkESl2T7bQZk1IzalX8X2aLMzWE7mPKv1yJ6fi2GB\nYLSWz/MOVJwe9bSFL6Ud1lYg+BXxSg42tSVs/spw0jmFA5dHjtlMyPL5DKyjEwsx\nCOfQRvob7wHkmGLQ+W12OwKBgQC71dhRv30RBeIbQVDbNs2AaMx3QYZzulkaRo5/\nwZJghpWXtsNXcWNLvNsphxgCtu8aBt0uKOw23KGoZoRhBSWGsW5d278gfcCY6DVh\nNuTLDgKxYGVQS1GzCPPTIuDjedYeSxdZWA63mPFpulvhTgEhNKYDJ/KqyCAjyckz\n2R8gqwKBgA/+FZkT30Y+6okRZUlT1KE6sTmLh7GXX5Ikm0I9agH7+B5ukUWhOkqU\npnCIwtO2duM+/Jaf0xtQ7hgrpRqjDjkog4gLK3mioFMYfR67heDFJrJJHCC2ZG1x\nPe0NQ3tZ9FJI+2bJRV+0u/Z1J4EVKHwHGMuJFdyYOaSCiLserVWRAoGBAKZ8XEfY\n2hmEhWxy8B/c6zitqszpHyrkOKW5dAR4pi04HM9kBrAyqDgxJHAidX2ydysyeki3\nrObTl9WTSDJWRXSlP5WheD5sN5FQAEAyT4hK2sgtEJ+ior91Z+f0OjBlhQtEs2VV\nT3Yb8Z4st9NzOD0eVSbm+Ye16gbOi6+Q+q4RAoGAV3VuT/LP59Ir6scGM8CeQTXC\nUG9mmJxe4slACJ5B5Ol0TDljGbH/bW035Ztnq8Frj9dTvjTD9kwjfu96pUysHIgo\nk43YFfmb/HlQvx/bTN2dOb7D7IAtjtF02s8WYVywKnc77aHLBPu/v7QY01GXpjAc\nnzg9NEgVReZPswQNzVg=',
    }
    payload = {'q': data, 'target': lang}
    response = requests.post("https://translation.googleapis.com/language/translate/v2", headers=headers, data=data)
    print(f'Receive Data: {data} in {lang}')
    return response.text
>>>>>>> Stashed changes

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