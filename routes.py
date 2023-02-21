from app import app
from dfs import objs
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/webcam')
def webcam():
    file = open(r'webcam.py', 'r').read()
    return render_template('webcam.html', results=exec(file))

@app.route('/dfs_response')
def run_deepface():
    file = open(r'dfs.py', 'r').read()
    print('My dictionary:', objs)
    return render_template('dfs_response.html', results=exec(file), value=objs)
# If the user inputs an invalid picture, prompt user to take another picture. Redirect to webcam. Continue this until user submits a valid picture. 
  




