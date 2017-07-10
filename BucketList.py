from flask import Flask, render_template, request, redirect, url_for
from classes.user import User
from classes.bucket import Bucket
from classes.activity import Activity

app = Flask(__name__)
all_buckets = []
all_activities = []


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
    return redirect(url_for('buckets'))


@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User()
        if user.sign_in(email, password):
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


@app.route('/buckets')
def buckets():
    return render_template('buckets.html',
                           buckets=all_buckets, len=len(all_buckets))


@app.route('/create_bucket', methods=["POST"])
def create_bucket():
    bucket_name = request.form['bucket-name']
    description = request.form['description']
    new_bucket = Bucket(bucket_name, description)
    all_buckets.append(new_bucket)
    return redirect(url_for('buckets', name='to_be_added'))


@app.route('/create_activity/<string:bucket_name>', methods=['POST'])
def create_activity(bucket_name):
    activity_name = request.form['activity-name']
    new_activity = Activity(activity_name)
    all_activities.append(new_activity)

    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    bucket[0].activities.append(new_activity)
    return redirect(url_for('activities',
                            bucket_name=bucket_name))


@app.route('/buckets/<string:bucket_name>')
def activities(bucket_name):
    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    bucket_activities = bucket[0].activities
    bucket_description = bucket[0].description
    return render_template('activities.html',
                           bucket_name=bucket_name,
                           bucket_acts=bucket_activities,
                           bucket_desc=bucket_description)


@app.route('/edit_bucket/<bucket_name>', methods=['POST'])
def edit_bucket(bucket_name):
    new_bucket_name = request.form['bucket-name']
    new_description = request.form['description']
    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    bucket[0].name = new_bucket_name
    bucket[0].description = new_description
    return redirect(url_for('activities',
                            bucket_name=new_bucket_name))


@app.route('/edit_activity/<string:bucket_name>/'
           '<string:activity_name>', methods=['POST', 'GET'])
def edit_activity(activity_name, bucket_name):
    if request.method == 'POST':
        new_activity_name = request.form['activity-name']

        found_bucket = [bucket for bucket in all_buckets
                        if bucket.name == bucket_name]
        activity = [activity for activity in found_bucket[0].activities
                    if activity.name == activity_name]
        activity[0].name = new_activity_name
        return redirect(url_for('activities',
                                bucket_name=bucket_name))
    else:
        return render_template('edit-activity.html',
                               bucket_name=bucket_name,
                               activity_name=activity_name)


@app.route('/del_bucket/<string:bucket_name>')
def delete_bucket(bucket_name):
    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    if bucket:
        all_buckets.remove(bucket[0])
        return redirect(url_for('buckets'))


@app.route('/del_activity/<string:bucket_name>/'
           '<string:activity_name>')
def del_activity(activity_name, bucket_name):
    bucket = [bucket for bucket in all_buckets
              if bucket.name == bucket_name]
    found_bucket = bucket[0]
    activity = [activity for activity in found_bucket.activities
                if activity.name == activity_name]
    found_bucket.activities.remove(activity[0])
    return redirect(url_for('activities',
                            bucket_name=bucket_name))


if __name__ == '__main__':
    app.run()
