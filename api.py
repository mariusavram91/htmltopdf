from flask import Flask
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    #config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_url('http://google.com', 'tmp/out.pdf')
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
