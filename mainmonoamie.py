from flask import Flask, render_template
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

@app.route('/login')
def login():
    form = Loginform()
    return render_template('Loginform.html', title='Sign In', form=form)
