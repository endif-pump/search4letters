from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return "Hi"

@app.route('/search4' ,methods=['POST'])
def do_search() -> str:
    pharse = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(pharse, letters))

@app.route('/entry' ,methods=['POST'])
def entry_page():
    return render_template('entry.html',
    the_title="Welcome search4letters")


app.run(debug=True)