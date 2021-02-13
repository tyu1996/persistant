from app import app
from flask import render_template, redirect

from .forms import SampleForm


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    title = "Persistant - Home"
    return render_template('index.html', title=title)


@app.route('/medication')
def medication():
    title = "Persistant - Medication"
    return render_template('medication.html', title=title)


@app.route('/groceries')
def groceries():
    title = "Persistant - Groceries"

    return render_template('groceries.html', title=title)


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = SampleForm()

    # If form is upon submission and is validated success
    if form.validate_on_submit():
        return redirect('index')

    return render_template('forms.html', form=form)
