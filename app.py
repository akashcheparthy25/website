from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "super_secret_key"

# Default user
users = {
    "admin": "admin"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return "Login Failed"

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f"Hi, welcome to Akash website, {session['username']}!"
    else:
        return redirect(url_for('login'))

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if 'username' in session:
        if request.method == 'POST':
            new_username = request.form['new_username']
            new_password = request.form['new_password']
            users[new_username] = new_password
            return "User created successfully!"
        return render_template('welcome.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
