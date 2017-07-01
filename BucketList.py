from flask import Flask, render_template, request, redirect, url_for
from classes.user import User

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/signUp', methods=['POST'])
def sign_up():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user = User()
    user.sign_up(name, email, password)
    return render_template('buckets.html', name=name)


@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User()
        if user.sign_in(email, password):
            return render_template('buckets.html', name=user.name)
        else:
            return render_template('signIn.html',
                                   error='Invalid username or password')
    else:
        return render_template('signIn.html')


@app.route('/signOut')
def sign_out():
    user = User()
    user.sign_out()


@app.route('/buckets')
def buckets():
    return render_template('buckets.html')


@app.route('/<string:bucket_name>')
def activities(bucket_name):
    return render_template('activities.html')


if __name__ == '__main__':
    app.run()
