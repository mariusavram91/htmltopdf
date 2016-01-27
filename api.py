from flask import Flask, make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    #config = pdfkit.configuration(wkhtmltopdf='bin/wkhtmltopdf')
    #pdfkit.from_url('http://google.com', 'tmp/out.pdf', configuration=config)
    return "Hello, World!"

@app.route('/download')
def index():
    config = pdfkit.configuration(wkhtmltopdf='bin/wkhtmltopdf')
    file_name = 'out.pdf'
    pdfkit.from_url('http://google.com', 'tmp/' + file_name, configuration=config)
    headers = {"Content-Disposition": "attachment; filename=%s" % file_name}
    with open('tmp/' + file_name, 'r') as f:
        body = f.read()
    return make_response((body, headers))

@app.route('/download_csv')
def download():
    csv = """"REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"
            "1985/01/21","Douglas Adams",0345391802,5.95
            "1990/01/12","Douglas Hofstadter",0465026567,9.95
            "1998/07/15","Timothy ""The Parser"" Campbell",0968411304,18.99
            "1999/12/03","Richard Friedman",0060630353,5.95
            "2004/10/04","Randel Helms",0879755725,4.50"""
    response = make_response(csv)
    response.headers["Content-Disposition"] = \
        "attachment; filename=books.csv"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
