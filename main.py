from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def home():
    data = None
    message = None
    return render_template('index.html', data=None, meessage=None)

@app.route('/', methods=['POST'])
def result():
    memory = BytesIO()
    link = request.form.get('link')
    if (link == ''):
        return render_template('index.html', message = 'Link cannot be empty' ,data=None)
    img = qrcode.make(link)
    img.save(memory)
    memory.seek(0)

    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
    return render_template('index.html', data=base64_img, message='Successfully generated QR Code')

if __name__ == '__main__':
    app.run(debug = True)
