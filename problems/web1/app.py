from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <title>flask debugger</title>
    </head>
    <body>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">flask debugger</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="/upload">upload</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav><br/><br/> 
    </body>
    '''
@app.route("/upload")
def upload():
    return '''
    <html>
    <body>
    <form action = "/fileupload" method = "POST"
        enctype = "multipart/form-data">
        <input type = "file" name = "file"/>
        <input type = "submit"/>
    </form>
    </body>    
    </html>
    '''

@app.route('/fileupload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      ext = f.filename[-3:]
      if ext == 'txt':
        f.save(f.filename)
        return f'''<form action = "/{f.filename}" method = "POST"
        enctype = "multipart/form-data">
        <input type = "submit"/>
        </form>'''
    return 'only .txt'

@app.route('/<path:file>', methods=['POST'])
def file(file):
	return open(file).read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
