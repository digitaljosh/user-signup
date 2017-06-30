from flask import Flask, render_template, request, redirect
import cgi



app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/confirmation", methods=['POST'])
def confirm():
    user = request.form['username']
    if (len(user) > 20) or (len(user) > 3) or (user == ""):
        error = "Username must be at least 3 characters long, no longer than 20 characters, and contain no spaces."
        return redirect("/?error=" + error)



    
    return render_template('confirmation.html', user = user)


@app.route("/")
def index():
    return render_template('home.html')


app.run()