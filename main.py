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

    if len(user) < 3 or len(user) > 20 or " " in user:
        error_username = "Username must be between 3 and 20 characters long and contain no spaces."
        return render_template("home.html", error_username = error_username)
    
    if len(password) < 3 or len(password) > 20 or " " in password:
        error_password = "Password must be between 3 and 20 characters long and contain no spaces."
        return render_template("home.html", error_password = error_password)

    if password_verify != password:
        error_verify = "Passwords don't match."
        return render_template("home.html", error_verify = error_verify)
    
    if email != "":
        at_symbol_count = email.count('@')
        period_count = email.count('.')
        if "@" not in email or "." not in email:
            error_email = "Invalid email"
            return render_template("home.html", error_email = error_email)
    
        if len(email) < 3 or len(email) > 20:
            error_email = "Invalid email"
            return render_template("home.html", error_email = error_email)

        if " " in email:
            error_email = "Invalid email"
            return render_template("home.html", error_email = error_email)

        if at_symbol_count > 1 or period_count > 1:
            error_email = "Invalid email - too many"
            return render_template("home.html", error_email = error_email)


        


        
    

    return render_template('confirmation.html', user = user)


@app.route("/")
def index():
    
    return render_template('home.html')

app.run()