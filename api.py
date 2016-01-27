import os
import pdfkit
import urllib
from flask import Flask, send_file, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("api")

@app.route('/api')
def api():
    return "Hello, World!"

@app.route('/api/download', methods=['GET'])
def download():
    config = pdfkit.configuration(wkhtmltopdf=os.environ['WKHTMLTOPDF_PATH'])
    output_name = str(request.args.get('output_name'))
    url = str(urllib.unquote(request.args.get('url').decode('utf8')))
    pdf = pdfkit.from_url(url, output_name, configuration=config)
    return send_file(output_name, as_attachment=True, mimetype='application/pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
