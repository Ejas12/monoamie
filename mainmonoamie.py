from flask import Flask, render_template, flash, redirect
from config import Config
from forms import Loginform
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hola %s' % username

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash('Usuario logueado {},'.format(form.username.data))
        return redirect('/')
    return render_template('Loginform.html', title='Sign In', form=form)
