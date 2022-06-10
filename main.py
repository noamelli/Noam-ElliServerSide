from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for('webRoot'))

@app.route('/webRoot')
def webRoot():
    user_info = {'FIRST Name': 'NOAM', 'Last Name': 'elli'}
    age=24.11        #there is a filter that round down the age
    hobbies=('music', 'cooking', 'food')
    #hobbies=()            #for checking what happens if i dont write any hobby
    return render_template('assignment3_1.html',
                           user_info=user_info,
                           age=age,
                           hobbies=hobbies
                           )

# root of our website
@app.route('/homepage')
def homePage():
    return render_template('homePage.html')


@app.route('/general')
def general_page():
    return render_template('GeneralPage.html')


@app.route('/form')
def form_output():
    return render_template('formOutPut.html')


@app.route('/contact')
def contact_us():
    return render_template('contactUs.html')


@app.route('/assignment3')
def assignment3():
    user_info = {'FIRST Name': 'NOAM', 'Last Name': 'elli'}
    age=24.11        #there is a filter that round down the age
    hobbies=('music', 'cooking', 'food')
    #hobbies=()            #for checking what happens if i dont write any hobby
    return render_template('assignment3_1.html',
                           user_info=user_info,
                           age=age,
                           hobbies=hobbies
                           )



if __name__ == '__main__':
    app.run(debug=True)
