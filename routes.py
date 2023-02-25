from app import app
from dfs import objs, run_dfs
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/webcam')
def webcam():
    file = open(r'webcam.py', 'r').read()
    return render_template('webcam.html', results=exec(file))
  
@app.route('/dfs_response')
def run_deepface():
    return render_template('dfs_response.html', value=run_dfs())


