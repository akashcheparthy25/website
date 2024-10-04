from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "super_secret_key"

# Default users (initial setup)
users = {
    "admin": "admin"  # Default admin user
}

# Route for login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists and password matches
        if username in users and users[username] == password:
            session['username'] = username
            print(f"User '{username}' successfully logged in.")  # Debugging statement
            return redirect(url_for('welcome'))
        else:
            print(f"Login attempt failed for user: {username}")  # Debugging statement
            return render_template('login.html', message="Invalid username or password")
    
    print("Rendering login page")  # Debugging statement
    return render_template('login.html')

# Route for welcome page after login
@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if 'username' in session:
        print(f"Displaying welcome page for user: {session['username']}")  # Debugging statement
        return render_template('welcome.html', username=session['username'])
    else:
        print("Redirecting to login page as session is not active.")  # Debugging statement
        return redirect(url_for('login'))

# Route for creating new user
@app.route('/create_user', methods=['POST'])
def create_user():
    if 'username' in session:
        new_username = request.form['new_username']
        new_password = request.form['new_password']

        # Check if the new user already exists
        if new_username in users:
            print(f"Attempt to create an existing user: {new_username}")  # Debugging statement
            return "User already exists!"

        # Add new user to the dictionary
        users[new_username] = new_password
        print(f"New user '{new_username}' created successfully.")  # Debugging statement
        return "User created successfully!"
    else:
        print("Redirecting to login as no active session found.")  # Debugging statement
        return redirect(url_for('login'))

# Route for logout
@app.route('/logout')
def logout():
    if 'username' in session:
        print(f"User '{session['username']}' logged out.")  # Debugging statement
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Start Flask application
    print("Starting Flask app...")  # Debugging statement
    app.run(host='0.0.0.0', port=5000)
