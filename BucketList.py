from flask import Flask, render_template, request, redirect, url_for, session
from classes.user import User
from classes.bucket import Bucket
from classes.item import Item
from classes.app import App

app = Flask(__name__)
app.secret_key = 'MySecretKey'
all_items = []
user = None
bucketApp = App()


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/signUp', methods=['POST'])
def sign_up():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user = User(name, email, password)
    session_id = bucketApp.sign_up(user)
    session['id'] = session_id
    return redirect(url_for('buckets'))


@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(email, password)
        session['id'] = bucketApp.sign_in(user)
        if session['id']:
            return redirect(url_for('buckets'))
        return render_template('signIn.html',
                               error='Invalid username or password')
    else:
        return render_template('signIn.html')


@app.route('/signOut')
def sign_out():
    bucketApp.sign_out()
    session.pop('email', None)
    return redirect(url_for('sign_in'))


@app.route('/buckets')
def buckets():
    """ 
    this funtion does xyz
    :params :   
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    return render_template('buckets.html',
                           buckets=user.all_buckets,
                           len=len(user.all_buckets))


@app.route('/create_bucket', methods=["POST"])
def create_bucket():
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    bucket_name = request.form['bucket-name']
    description = request.form['description']
    new_bucket = Bucket(bucket_name, description, session['id'])
    user.create_bucket(new_bucket)
    return redirect(url_for('buckets', name='to_be_added'))




if __name__ == '__main__':
    app.run()
