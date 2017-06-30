from flask import Flask, request, redirect, render_template
import cgi



app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/confirmation", methods=['POST'])
def confirm():
    user = request.form['username']
    password = request.form['password']
    password_verify = request.form['verify']
    email = request.form['email']

    if len(user) < 3 or len(user) > 20 or user == "":
        error = "Username must be between 3 and 20 characters long and contain no spaces."
        return redirect("/?error=" + error)
    
    if len(password) < 3 or len(password) > 20 or password == "":
        error = "Password must be between 3 and 20 characters long and contain no spaces."
        return redirect("/?error=" + error)

    if password_verify != password:
        error = "Password verification must match password."
        return redirect("/?error=" + error)
    
    if email != "":
        if "@" not in email or "." not in email:
            error = "Invalid email"
            return redirect("/?error=" + error)
    
        if len(email) < 3 or len(email) > 20:
            error = "Invalid email"
            return redirect("/?error=" + error)

    

    



    
    return render_template('confirmation.html', user = user)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('home.html', error=encoded_error and cgi.escape(encoded_error, quote=True))


app.run()