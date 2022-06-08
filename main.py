from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template

app = Flask(__name__)

# root of our website
@app.route('/')
def website_root():
    return render_template('contactUs.html')

@app.route('/general')
def general_page():
    return render_template('GeneralPage.html')


@app.route('/form')
def form_output():
    return render_template('formOutPut.html')


@app.route('/contact')
def contact_us():
    return render_template('contactUs.html')


@app.route('/homepage')
def home_page():
    return render_template('homePage.html')


if __name__ == '__main__':
    app.run(debug=True)
