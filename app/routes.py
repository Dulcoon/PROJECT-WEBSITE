from flask import Flask

from flask import Flask, render_template, request, redirect, url_for, flash
# from app import app

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
