import os, io
import openai
from flask import Flask, redirect, render_template, request, url_for, abort, send_file
from werkzeug.utils import secure_filename
from markupsafe import escape

from backend.createsheet import create_sheet

app = Flask(__name__)
openai.api_key = ("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")

UPLOAD_FOLDER = "tmp"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']


@app.route("/", methods = ["GET", "POST"])
def get_file():
    print(openai.api_key)
    if request.method == "POST":
        f = request.files['file']
        filename = secure_filename(f.filename)
        if filename != '':
            ext = os.path.splitext(filename)[1]
            filename = filename + app.config["UPLOAD_FOLDER"]
            if ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            f.save(filename)

            return_data = io.BytesIO()
            with open(filename, 'rb') as fo:
                return_data.write(fo.read())
            return_data.seek(0)
            os.remove(filename)

            return create_sheet(return_data)
        
    abort(400)

@app.route("/download")
def download():
    filename = app.config['UPLOAD_FOLDER'] + "mastersheet"

    return_data = io.BytesIO()
    with open(filename, 'rb') as fo:
        return_data.write(fo.read())
    return_data.seek(0)

    os.remove(filename)

    return send_file(return_data, mimetype="application/pdf", 
                     download_name='mastersheet.pdf', as_attachment=True)

@app.route("/upload", methods = ["GET", "POST"])
def upload():
    if (request.method == "POST"):
        data = str(request.data)
    else:
        data = "This is a test"

    with open(app.config['UPLOAD_FOLDER'] + "mastersheet", "w") as fo:
        fo.write(data)

    return redirect(url_for('download'))