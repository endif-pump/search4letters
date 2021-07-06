from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters


app = Flask(__name__)




@app.route('/search4' ,methods=['POST'])
def do_search() -> str:
    pharse = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(pharse, letters))
    log_request(request, results)
    return results

@app.route('/')
@app.route('/entry' ,methods=['POST'])
def entry_page():
    return render_template('entry.html',
    the_title="Welcome search4letters")

@app.route('/logs')
def view_log() -> str:
    with open('searchlog') as log:
        contents = log.read()
    return escape(contents)

def log_request(req: 'flask_request', res: str) -> None:
    with open('searchlog', 'a') as log:
        print(req.form,  file=log, end='|')
        print(req.remote_addr,  file=log, end='|')
        print(req.user_agent,  file=log, end='|')
        print(res,  file=log)

if __name__ == '__main__':
    app.run(debug=True)