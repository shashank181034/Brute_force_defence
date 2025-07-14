from flask import Flask, request, render_template_string, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_session import Session
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "batcave-secret"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Apply rate limiting: 5 attempts per minute per IP
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "batman123"

# HTML template with CAPTCHA
html = '''
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method="POST">
  Username: <input type="text" name="username"><br><br>
  Password: <input type="password" name="password"><br><br>
  Captcha: What is 5 + 3? <input type="text" name="captcha"><br><br>
  <input type="submit" value="Login">
</form>
<p>{{ message }}</p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''

    # Track failed attempts in session
    if 'attempts' not in session:
        session['attempts'] = 0

    # Lock account after 3 failed attempts
    if session['attempts'] >= 3:
        message = '⚠️ Too many failed attempts. Account locked.'
    elif request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        captcha = request.form.get('captcha')

        # Check CAPTCHA
        if captcha != '8':
            message = '🤖 CAPTCHA failed.'
        elif user == USERNAME and pw == PASSWORD:
            message = '✅ Login successful!'
            session['attempts'] = 0  # Reset attempts
        else:
            session['attempts'] += 1
            message = f'❌ Invalid credentials. Attempt {session["attempts"]}/3'

            # Log failed attempt
            with open("login_attempts.log", "a") as log:
                log.write(f"[{datetime.datetime.now()}] Failed login from IP: {request.remote_addr}, Username: {user}, Password: {pw}\n")

    return render_template_string(html, message=message)

if __name__ == '__main__':
    app.run(debug=True)
