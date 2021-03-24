from flask import Flask, render_template, request, escape
from search4.search4letters import search4letters

from DBcm import UseDatabase
app = Flask(__name__)
db_config = {'host': '127.0.0.1', 'user': 'vsearch', 'database': 'vsearchlogDB'}

def log_request(req: 'flask_request', res: str) -> None:

    with UseDatabase(db_config) as cursor:
        _SQL = """insert into log (phrase, letters, ip, browser_string, results) values 
                (%s,%s,%s,%s,%s)"""
        cursor.execute(_SQL, (req.form["phrase"], req.form["letters"], req.remote_addr, req.user_agent.browser, res))


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_title="Results", the_phrase=phrase, the_letters=letters,
                           the_results=result)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> 'html':
    with UseDatabase(db_config) as cursor:
        _SQL = """SELECT phrase, letters, ip, browser_string, results FROM log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    return render_template('viewlog.html', the_title=" User log ", logs=contents)


while __name__ == "__main__":
    app.run(debug=True)
