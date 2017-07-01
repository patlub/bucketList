from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/signUp', methods=['POST'])
def sign_up():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user = [name, email, password]
    if user:
        return render_template('buckets.html', name=name)


@app.route('/signIn', methods=['POST', 'GET'])
def sign_in():
    email = 'patricklu2010@gmail.com'
    password = 'patrick'
    name = 'Patrick'
    if request.method == 'POST':
        if request.form['email'] == email \
                and request.form['password'] == password:
            return render_template('buckets.html', name=name)
        else:
            return render_template('signIn.html',
                                   error='Invalid username or password')
    else:
        return render_template('signIn.html')


@app.route('/buckets')
def buckets():
    return render_template('buckets.html')


@app.route('/<string:bucket_name>')
def activities(bucket_name):
    return render_template('activities.html')


if __name__ == '__main__':
    app.run()
