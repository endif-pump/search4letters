from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
from DBcm import UseDatabase
import pymysql

dbconfig = {
    'host': '172.17.0.2',
    'user': 'root',
    'password': 'my-secret-pw',
    'database': 'searchlogDB',
} 



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
    with UseDatabase(dbconfig) as cursor:

        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
    
        cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, ))


if __name__ == '__main__':
    app.run(debug=True)