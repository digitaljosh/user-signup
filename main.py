from flask import Flask, render_template, request, redirect
import cgi



app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/confirmation", methods=['POST'])
def confirm():
    user = request.form['username']
    return render_template('confirmation.html', user = user)


@app.route("/")
def index():
    return render_template('home.html')


app.run()