from flask import Flask, url_for, render_template, request, make_response, redirect, abort, session, g, flash
import sqlite3
from config import *

app = Flask(__name__)
app.config.from_object(config['development'])
cf = config['development']


def connect_db():
    rv = sqlite3.connect(cf.DATABASE)
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def close_db(error):
    print('close')

    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title,text from entries order by id desc ')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_id'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title,text) values (?,?)', [request.form['title'], request.form['text']])
    db.commit()
    flash('new entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != cf.USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != cf.PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_id'] = True
            flash('you were logged in ')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_id', None)
    flash('you were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    init_db()
    app.run()
