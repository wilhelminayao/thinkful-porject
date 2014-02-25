# -*- coding: utf-8 -*-
import os
import mimetypes
from tempfile import mktemp
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, redirect, url_for
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/Uploads'
ALLOWED_MIMETYPES = {'image/jpeg', 'image/png', 'image/gif'}
 
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html', img='')
    elif request.method == 'POST':
        f = request.files['file']
        fname = mktemp(suffix='_', prefix='u', dir=UPLOAD_FOLDER) + secure_filename(f.filename)
        f.save(fname)
        if mimetypes.guess_type(fname)[0] in ALLOWED_MIMETYPES:
            return render_template('upload.html', img=fname)
        else:
            os.remove(fname)
            return redirect(url_for('upload'), 302)
 
@app.route('/')
def index():
    return redirect(url_for('upload'), 302)
 
if __name__ == '__main__':
    app.run(debug=True)