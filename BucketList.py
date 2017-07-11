from flask import Flask, render_template, request, redirect, url_for, session, flash
from classes.user import User
from classes.bucket import Bucket
from classes.item import Item
from classes.app import App

app = Flask(__name__)
app.secret_key = 'MySecretKey'
all_items = []
current_user = None
bucketApp = App()


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/signUp', methods=['POST'])
def sign_up():
    """
    Signs up user to the app
    """

    # Pick form values
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # create user
    global current_user
    current_user = User(name, email, password)
    session_id = bucketApp.sign_up(current_user)
    # start session
    session['id'] = session_id
    return redirect(url_for('buckets'))


@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    """
    Signs in user to their account
    """
    if request.method == 'POST':
        # Pick form values
        email = request.form['email']
        password = request.form['password']
        global current_user
        current_user = User(email, password)
        # start session
        session['id'] = bucketApp.sign_in(current_user)
        if session['id']:
            return redirect(url_for('buckets'))
        return render_template('signIn.html',
                               error='Invalid username or password')
    else:
        return render_template('signIn.html')


@app.route('/signOut')
def sign_out():
    """
    Signs out user
    """
    session.pop('id', None)
    return redirect(url_for('sign_in'))


@app.route('/buckets')
def buckets():
    """ 
    Returns list of all buckets   
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))

    user = [user for user in bucketApp.all_users
            if user.id == session['id']]
    if user:
        return render_template('buckets.html',
                               buckets=user[0].get_buckets(),
                               len=len(user[0].get_buckets()))
    else:
        return redirect(url_for('sign_in'))


@app.route('/create_bucket', methods=["POST"])
def create_bucket():
    """
    Creates a new bucket list
    :return: 
    """

    # Check user is signed in
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    # Pick form values
    bucket_name = request.form['bucket-name']
    description = request.form['description']
    # create bucket
    new_bucket = Bucket(bucket_name, description, session['id'])
    global current_user
    if current_user.create_bucket(new_bucket):
        return redirect(url_for('buckets'))
    flash('Bucket name already exists')
    return redirect(url_for('buckets'))


if __name__ == '__main__':
    app.run()
