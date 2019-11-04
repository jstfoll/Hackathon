from flask import Flask,request,url_for,redirect,render_template,flash, send_from_directory
import os
import jinja2
import json
import datetime
from werkzeug.utils import secure_filename
from pathlib import Path
import platform
import requests

app = Flask(__name__, static_url_path='')
if platform.system() == 'Windows':
    UPLOAD_FOLDER = Path(__file__).parent.joinpath('uploads')
else:
    UPLOAD_FOLDER = r'uploads'




@app.route('/')
def homepage():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        data = request.form.to_dict(flat= True)
        print(data)
        return "Success"




	
if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)