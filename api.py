from flask import Flask
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    #config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    #pdfkit.from_url('http://google.com', 'out.pdf', configuration=config)
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
