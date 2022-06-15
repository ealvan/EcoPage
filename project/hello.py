from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/')
def index():
    return 'MY Index Page'

#VARIABLE RULES.........................................
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
# @app.route('/hello')
# def hello():
#     return 'Hello, World'
# string # (default) accepts any text without a slash

# int # accepts positive integers

# float # accepts positive floating point values

# path # like string but also accepts slashes

# uuid # accepts UUID strings
##########################################3333
#REDIRECTION BEHAVIOUR

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
###################################USE OF -> url_for()
#give a absolute path
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
@app.route('/login')
def login():
    return 'login'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello',name='PEPE'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


