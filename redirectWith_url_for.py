# A flask app where a username is given in the URL, using 'user/<username>'
# If the un is 'admin,' it redirects to site saying "Hello Admin"
# Otherwise, it directes to site saying "Hello [name of guest] as guest"

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin/')
def admin_hello_page():
    return "Hello admin"

@app.route('/guest/<name>/')
def guest_hello_page(name):
    return 'Hello %s as guest' % name

@app.route('/<username>/')
def sign_in(username):
    if username == 'admin':
        return redirect(url_for('admin_hello_page'))
    else:
        return redirect(url_for('guest_hello_page', name=username))
    
if __name__ == '__main__':
    app.run(debug=True)