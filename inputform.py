from flask import Flask, render_template, url_for, request, session, redirect
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://'
mongo = PyMongo(app)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/create" enctype="multipart/form-data">
            <input type="text" name="username">
            <input type="file" name="upload_file">
            <input type="submit">
        </form>
    '''

@app.route('/create', methods=["POST"])
def create():
    if 'upload_file' in request.files:
        upload_file = request.files['upload_file']
        mongo.save_file(upload_file.filename, upload_file)
        mongo.db.users.insert({'username' : request.form.get('username'), 'upload_image_name' : upload_file.filename})

    return 'Information uploaded'

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/profile/<username>')
def profile(username):
    user = mongo.db.users.find_one_or_404({'username' : username})
    return '''
    <h1>{username}</h1>
    <img src""
'''
