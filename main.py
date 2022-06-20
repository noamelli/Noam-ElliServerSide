from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from flask import request, session, jsonify
from datetime import timedelta

app = Flask(__name__)

app.secret_key = '473'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1440)


@app.route('/')
def root():
    return redirect('/homepage')


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


# assigment 3_1- the button of this page called "about me"
@app.route('/assignment3_1')
def assignment3_1():
    user_info = {'FIRST Name': 'NOAM', 'Last Name': 'elli'}
    age = 24.11  # there is a filter that round down the age
    hobbies = ('music', 'cooking', 'food')
    # hobbies=()      #for checking what happens if i dont write any hobby: serves for qestion 3c in part B
    return render_template('assignment3_1.html',
                           user_info=user_info,
                           age=age,
                           hobbies=hobbies
                           )


# assigment 3_2 - the button of this page called "search for" / " register"
# search form
@app.route('/assignment3_2')
def assignment3_2():
    return render_template('assignment3_2.html')


user_dict = {
    'yosi': {'nickName': 'yosiC', 'lastName': 'cohen', 'email': 'yosi@gmail.com', 'password': '475333'},
    'li': {'nickName': 'lico', 'lastName': 'coren', 'email': 'li90@gmail.com', 'password': '231111'},
    'ido': {'nickName': 'idodo', 'lastName': 'dor', 'email': 'idor@gmail.com', 'password': '222444'},
    'neta': {'nickName': 'dubi', 'lastName': 'meir', 'email': 'sati@gmail.com', 'password': '234235'},
    'noam': {'nickName': 'noami', 'lastName': 'elli', 'email': 'noami@gmail.com', 'password': '123456'}
}


@app.route('/searchForm', methods=['GET'])
def searchForm():
    if 'fname' in request.args:
        first_name = request.args['fname']
        if first_name in user_dict:
            return render_template('assignment3_2.html',
                                   first_name=first_name,
                                   last_name=user_dict[first_name]['lastName'],
                                   nickName=user_dict[first_name]['nickName'],
                                   email=user_dict[first_name]['email'])
        elif (first_name == ""):
            return render_template('assignment3_2.html',
                                   user_dict=user_dict)
        else:
            return render_template('assignment3_2.html',
                                   message='The user is not found!')


# registration form
@app.route('/registerForm', methods=['POST', 'GET'])
def register_func():
    if request.method == 'POST':
        nickName = request.form['nickName']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        for k in user_dict:
            if user_dict[k]['email'] == email:
                return render_template('assignment3_2.html', message2="This user is already exist")
            else:
                newUser = {
                    firstName: {'nickName': nickName, 'lastName': lastName, 'email': email, 'password': password}}
                user_dict.update(newUser)
                session['nickName'] = nickName
                session['logedin'] = True
                return render_template('assignment3_2.html',
                                       nickName=nickName,
                                       firstName=firstName,
                                       lastName=lastName,
                                       password=password)
    return redirect(url_for('assignment3_2'))


@app.route('/session')
def session_func():
    return jsonify(dict(session))


@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('assignment3_2'))


if __name__ == '__main__':
    app.run(debug=True)
