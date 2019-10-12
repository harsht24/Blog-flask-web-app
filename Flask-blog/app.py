from flask import Flask, render_template, url_for
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

app.config['SECRET KEY'] = '7d8b3a101a9e8019ed0d9986f5e67a64'

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


if __name__ == '__main__':
    app.run(debug=True)
