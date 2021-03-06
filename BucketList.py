from datetime import time, date
from time import strftime, gmtime

from flask import Flask, render_template, \
    request, redirect, url_for, session, flash
from classes.user import User
from classes.bucket import Bucket
from classes.item import Item
from classes.app import App

app = Flask(__name__)
app.secret_key = 'MySecretKey'
all_items = []
current_user = None
bucketApp = App()


@app.route('/', methods=['GET'])
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
    current_user = User(email, password, name)
    session['id'] = bucketApp.sign_up(current_user)
    # start session
    if session['id']:
        return redirect(url_for('buckets'))
    else:
        return render_template('index.html', error='Email already exists')


@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    """
    Signs in user to their account
    """
    if request.method == 'POST':
        # Pick form values
        email = request.form['email']
        password = request.form['password']
        user = User(email, password)
        # start session
        session['id'] = bucketApp.sign_in(user)

        if session['id']:
            global current_user
            user = [user for user in bucketApp.all_users
                    if user.id == session['id']]
            current_user = user[0]

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
    global current_user
    return render_template('buckets.html',
                           buckets=current_user.get_buckets())


@app.route('/create_bucket', methods=["POST"])
def create_bucket():
    """
    Creates a new bucket list 
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


@app.route('/edit_bucket/<bucket_name>', methods=['POST'])
def edit_bucket(bucket_name):
    """
    Edits attributes of a bucket
    :param bucket_name: 
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    new_bucket_name = request.form['bucket-name']
    new_description = request.form['description']
    global current_user
    current_user.edit_bucket(bucket_name,
                             new_bucket_name, new_description)
    return redirect(url_for('single_bucket',
                            bucket_name=new_bucket_name))


@app.route('/buckets/<string:bucket_name>')
def single_bucket(bucket_name):
    """
    Returns a single bucket with a given name
    :param bucket_name: 
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    global current_user
    bucket = current_user.get_single_bucket(bucket_name)
    return render_template('items.html',
                           bucket_name=bucket_name,
                           bucket_items=bucket.items,
                           bucket_desc=bucket.description)


@app.route('/del_bucket/<string:bucket_name>')
def delete_bucket(bucket_name):
    """
    Deletes a bucket from bucket list
    :param bucket_name: 
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    global current_user
    current_user.delete_bucket(bucket_name)
    return redirect(url_for('buckets'))


@app.route('/create_item/<string:bucket_name>', methods=['POST'])
def create_item(bucket_name):
    """
    Creates a bucket
    :param bucket_name:  
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    item_name = request.form['item-name']
    date_added = strftime("%Y-%m-%d", gmtime())
    new_item = Item(item_name, date_added)
    global current_user
    current_user.add_item(bucket_name, new_item)
    return redirect(url_for('single_bucket',
                            bucket_name=bucket_name))


@app.route('/edit_item/<string:bucket_name>/'
           '<item_name>', methods=['POST', 'GET'])
def edit_item(item_name, bucket_name):
    """
    Edits an item in a given bucket
    :param item_name: 
    :param bucket_name: 
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    if request.method == 'POST':
        new_item_name = request.form['item-name']
        status = False
        if 'status' in request.form:
            status = request.form['status']
        global current_user
        current_user.edit_item(bucket_name, item_name,
                               new_item_name, status)
        return redirect(url_for('single_bucket',
                                bucket_name=bucket_name))
    else:
        item = current_user.get_single_item(bucket_name, item_name)
        return render_template('edit-item.html',
                               bucket_name=bucket_name,
                               activity_name=item_name,
                               status=item.status)


@app.route('/del_item/<string:bucket_name>/'
           '<string:item_name>')
def del_item(item_name, bucket_name):
    """
    Deletes an item from a bucket
    :param item_name: 
    :param bucket_name: 
    """
    if 'id' not in session:
        return redirect(url_for('sign_in'))
    global current_user
    current_user.delete_item(bucket_name, item_name)
    return redirect(url_for('single_bucket',
                            bucket_name=bucket_name))


if __name__ == '__main__':
    app.run()
