#this code is from https://github.com/RaktimBhuiya/flask-app-ecs.git
#Flask App
#Modify Line 3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return node
if nne:
    go


@app.route('/health')
def health():
    return 'Server is up and running'
