from flask import Flask

app = Flask(__name__)

from routes import *
# imports all code from routes.py 

if __name__ == '__main__':
    app.run(debug=True)
