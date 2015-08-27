from datetime import datetime

from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, flash

from config import config
from forms  import NameForm


app = Flask(__name__)

app.config.update(config)


@app.route('/', methods=['GET', 'POST'])
def index():
  form = NameForm()

  if form.validate_on_submit():
    notify(session.get('name'), form.name.data)
    session['name'] = form.name.data
    return redirect(url_for('index'))

  return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
  return (render_template('404.html'), 404)


@app.errorhandler(500)
def internal_server_error(e):
  return (render_template('500.html'), 500)


def notify(previous_name, new_name):
  """Notify the user when her name changes."""

  if previous_name is not None and previous_name != new_name:
    flash('Looks like you have changed your name.')
