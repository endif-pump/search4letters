from flask import Flask, render_template, request, redirect, escape, session
from vsearch import search4letters
from DBcm import UseDatabase
import pymysql

dbconfig = {
    'host': '172.17.0.2',
    'user': 'root',
    'password': 'my-secret-pw',
    'database': 'searchlog',
}

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    pharse = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(pharse, letters))
    log_request(request, results)
    return results


@app.route('/')
@app.route('/entry', methods=['POST'])
def entry_page():
    return render_template('entry.html', the_title="Welcome search4letters")


@app.route('/logs')
def view_log() -> str:
    contents = ''
    with UseDatabase(dbconfig) as cursor:

        _SQL = """SELECT phrase, letters, ip, browser_string, results FROM log"""
        cursor.execute(_SQL )
        contents = cursor.fetchall()
        print(contents)
    return escape(contents)
        


def log_request(req: 'flask_request', res: str) -> None:
    with UseDatabase(dbconfig) as cursor:

        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""

        cursor.execute(_SQL, (
            req.form['phrase'],
            req.form['letters'],
            req.remote_addr,
            req.user_agent.browser,
            res,
        ))


if __name__ == '__main__':
    app.run(debug=True)