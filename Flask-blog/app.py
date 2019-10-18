from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '7d8b3a101a9e8019ed0d9986f5e67a64'

posts = [
    {
        'author': 'Harsh Tamkiya',
        'title': 'Blog post 1',
        'content': 'Data science',
        'date_posted': 'Oct 10, 2019'
    },
    {
        'author': 'Eden Hazard',
        'title': 'Blog post 2',
        'content': 'New start at Madrid',
        'date_posted': 'Oct 11, 2019'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','sucecss')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
