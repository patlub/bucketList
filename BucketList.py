from flask import Flask, render_template, request, redirect, url_for, session
from classes.user import User
from classes.bucket import Bucket
from classes.item import Item

app = Flask(__name__)
app.secret_key = 'MySecretKey'
all_buckets = []
all_items = []


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
    session['email'] = email
    return redirect(url_for('buckets'))


@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User()
        if user.sign_in(email, password):
            session['email'] = email
            return redirect(url_for('buckets'))
        else:
            return render_template('signIn.html',
                                   error='Invalid username or password')
    else:
        return render_template('signIn.html')


@app.route('/signOut')
def sign_out():
    user = User()
    user.sign_out()
    session.pop('email', None)
    return redirect(url_for('sign_in'))


@app.route('/buckets')
def buckets():
    if 'email' not in session:
        return redirect(url_for('sign_in'))
    return render_template('buckets.html',
                           buckets=all_buckets, len=len(all_buckets))


@app.route('/create_bucket', methods=["POST"])
def create_bucket():
    if 'email' not in session:
        return redirect(url_for('sign_in'))
    bucket_name = request.form['bucket-name']
    description = request.form['description']
    new_bucket = Bucket(bucket_name, description)
    all_buckets.append(new_bucket)
    return redirect(url_for('buckets', name='to_be_added'))


@app.route('/create_activity/<string:bucket_name>', methods=['POST'])
def create_activity(bucket_name):
    if 'email' not in session:
        return redirect(url_for('sign_in'))
    item_namm = request.form['activity-name']
    new_item = Item(item_namm)
    all_items.append(new_item)

    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    bucket[0].items.append(new_item)
    return redirect(url_for('items',
                            bucket_name=bucket_name))


@app.route('/buckets/<string:bucket_name>')
def items(bucket_name):
    if 'email' not in session:
        return redirect(url_for('sign_in'))
    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    bucket_items = bucket[0].items
    bucket_description = bucket[0].description
    return render_template('activities.html',
                           bucket_name=bucket_name,
                           bucket_acts=bucket_items,
                           bucket_desc=bucket_description)


@app.route('/edit_bucket/<bucket_name>', methods=['POST'])
def edit_bucket(bucket_name):
    if 'email' not in session:
        return redirect(url_for('sign_in'))
    new_bucket_name = request.form['bucket-name']
    new_description = request.form['description']
    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    bucket[0].name = new_bucket_name
    bucket[0].description = new_description
    return redirect(url_for('items',
                            bucket_name=new_bucket_name))


@app.route('/edit_activity/<string:bucket_name>/'
           '<string:activity_name>', methods=['POST', 'GET'])
def edit_item(activity_name, bucket_name):
    if 'email' not in session:
        return redirect(url_for('sign_in'))
    if request.method == 'POST':
        new_item_name = request.form['activity-name']

        found_bucket = [bucket for bucket in all_buckets
                        if bucket.name == bucket_name]
        item = [item for item in found_bucket[0].items
                if item.name == activity_name]
        item[0].name = new_item_name
        return redirect(url_for('items',
                                bucket_name=bucket_name))
    else:
        return render_template('edit-activity.html',
                               bucket_name=bucket_name,
                               activity_name=activity_name)


@app.route('/del_bucket/<string:bucket_name>')
def delete_bucket(bucket_name):
    if 'email' not in session:
        return redirect(url_for('sign_in'))
    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    if bucket:
        all_buckets.remove(bucket[0])
        return redirect(url_for('buckets'))


@app.route('/del_activity/<string:bucket_name>/'
           '<string:activity_name>')
def del_item(activity_name, bucket_name):
    if 'email' not in session:
        return redirect(url_for('sign_in'))
    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    found_bucket = bucket[0]
    item = [item for item in found_bucket.items
            if item.name == activity_name]
    found_bucket.items.remove(item[0])
    return redirect(url_for('items',
                            bucket_name=bucket_name))


if __name__ == '__main__':
    app.run()
