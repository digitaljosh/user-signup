from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/confirmation", methods=['POST', 'GET'])
def confirm():
    user = request.form['username']
    password = request.form['password']
    password_verify = request.form['verify']
    email = request.form['email']

    error_username = ""
    error_password = ""
    error_verify = ""
    error_email = ""

    at_symbol_count = email.count('@')
    period_count = email.count('.')

    if len(user) < 3 or len(user) > 20 or " " in user :
        error_username = "Invalid username."
        error_username = error_username
    
    if len(password) < 3 or len(password) > 20 or " " in password:
        error_password = "Invalid password."
        error_password = error_password

    if password_verify != password:
        error_verify = "Passwords don't match."
        error_verify = error_verify

    if len(email) > 0:
        if len(email) < 3 or len(email) > 20:
            error_email = "Invalid email: too short or too long"
            error_email = error_email

    if " " in email:
        error_email = "Invalid email: spaces not accepted"
        error_email = error_email

    if at_symbol_count > 1 or period_count > 1:
        error_email = "Invalid email: extra character"
        error_email = error_email
    
    if email.isalpha:
        if '@' not in email or '.' not in email:
            error_email = "Invalid email: missing character"
            error_email = error_email

    if not error_username and not error_password and not error_verify and not error_email:
        return render_template('confirmation.html', user=user)

    else:
        return render_template('home.html', error_username=error_username, error_password=error_password, error_verify=error_verify, error_email=error_email)


@app.route("/")
def index():
    
    return render_template('home.html')

app.run()