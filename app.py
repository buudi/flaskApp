from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jajaja'
app.permanent_session_lifetime = timedelta(seconds=5)

class FormThingy(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    submit = SubmitField('submit')

@app.route('/',methods=['GET','POST'])
def index(): 
    global form
    global namePrintedx
    namePrinted = 'stranger'
    session.permanent = True
    form = FormThingy()
    if form.validate_on_submit():
        namePrinted = form.name.data
        form.name.data = '' 
        session['name'] = namePrinted
        return redirect(url_for('welcome'))
    else:
        return render_template('index.html',namePrinted=namePrinted,form=form)
      

@app.route('/welcome')
def welcome():
    return render_template('index.html',form=form,namePrinted=session.get('name'))

if __name__ == '__main__' :
    app.run()