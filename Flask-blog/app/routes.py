from flask import render_template, url_for, flash, redirect
from app.forms import RegisterationForm, LoginForm
from app.model import User, Post
from app import app, db, bcrypt
from flask_login import login_user

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
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. Please login first. {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
