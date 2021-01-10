from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/orgregister.html')
def orgregister():
    return render_template('orgregister.html')

@app.route('/volpositions.html')
def volpositions():
    return render_template('volpositions.html')