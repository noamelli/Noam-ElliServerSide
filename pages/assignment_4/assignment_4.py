import random

from flask import render_template, Blueprint
from flask import Flask, redirect, render_template
from flask import url_for
from flask import request, session, jsonify
from datetime import timedelta
import mysql.connector
import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

assignment_4 = Blueprint('assignment_4', __name__,
                         static_folder='static',
                         static_url_path='/pages/assignment_4',
                         template_folder='templates')

assignment_4.secret_key = '123'


@assignment_4.route('/')
def root():
    return redirect('/assignment_4')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host=os.getenv('DB_HOST'),
                                         user=os.getenv('DB_USER'),
                                         passwd=os.getenv('DB_PASSWORD'),
                                         database=os.getenv('DB_NAME'))
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    data = 'select * from users'
    users_list_for_check = interact_db(data, query_type='fetch')
    email = request.form['mail']
    for user in users_list_for_check:
        if email == user.email:
            session['message'] = 'The user is already exists in the data base'
            return redirect('/showMessage')
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    nickName = request.form['nickName']
    password = request.form['password']
    query = "INSERT INTO users(email, FirstName,LastName,Nickname, password_) VALUES ('%s', '%s', '%s','%s','%s')" % (
        email, firstName, lastName, nickName, password)
    interact_db(query=query, query_type='commit')
    session['message'] = 'The user was added to the data base'
    return redirect('/showMessage')


@assignment_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    data = 'select * from users'
    users_list_for_check = interact_db(data, query_type='fetch')
    emailForDelete = request.form['email']
    for user in users_list_for_check:
        if emailForDelete == user.email:
            query = "DELETE FROM users WHERE email='%s';" % emailForDelete
            interact_db(query=query, query_type='commit')
            session['message'] = 'The user was deleted from the data base '
            return redirect('/showMessage')
    session['message'] = 'The user you asked to delete was not found in the data base '
    return redirect('/showMessage')


@assignment_4.route('/update_user', methods=['POST'])
def update_user():
    data = 'select * from users'
    users_list_for_check = interact_db(data, query_type='fetch')
    firstName = request.form['Fname']
    lastName = request.form['Lname']
    nickName = request.form['nick']
    email = request.form['mail_']
    password = request.form['pass']
    for user in users_list_for_check:
        if email == user.email:
            query = "UPDATE users SET email ='%s', FirstName ='%s',LastName='%s',Nickname= '%s',password_= '%s' WHERE email='%s';" % (
                email, firstName, lastName, nickName, password, email)
            interact_db(query=query, query_type='commit')
            session['message'] = 'The user details were updated '
            return redirect('/showMessage')
    session['message'] = 'The user you asked to update his details was not found in the data base '
    return redirect('/showMessage')


@assignment_4.route('/showMessage')
def showMess():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)


@assignment_4.route('/assignment_4')
def users():
    session.clear()
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)


@assignment_4.route('/assignment4/users')
def json_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return jsonify(users_list)


#########


def save_users_to_session(user):
    user_dictionary = {
        'id': user['data']['id'],
        'firstName': user['data']['first_name'],
        'lastName': user['data']['last_name'],
        'email': user['data']['email'],
        'avatar': user['data']['avatar']

    }
    session['users'] = user_dictionary


def get_users_sync(id_be):
    res = requests.get(f'https://reqres.in/api/users/ {id_be}')
    print(res)
    user = res.json()
    return user


@assignment_4.route('/assignment4/outer_source')
def fetch_user():
    if 'id_be' in request.args:
        id_be = request.args['id_be']
        session['id_be'] = id_be
        user = get_users_sync(id_be)
        save_users_to_session(user)
    else:
        session.clear()
    return render_template('assignment4partB.html')


@assignment_4.route('/assignment4/restapi_users', defaults={'ID': 1})
@assignment_4.route('/assignment4/restapi_users/<int:ID>')
def restapi_users(ID):
    query = f'select * from users_partc where users_partc.ID={ID}'
    user_list = interact_db(query, query_type='fetch')

    if len(user_list) == 0:
        return_dict = {
            'message': 'the user was not found  in the data base '
        }
        return(return_dict)
    else:
        user_list = user_list[0]
        return_dict = {'first_name': user_list.firstName,
                       'last_name': user_list.lastName}
        return jsonify(return_dict)

#users -insert query
# insert into users (email, FirstName,LastName,Nickname, password_) VALUES
# ('yosi@gmail.com', 'yosi', 'cohen','yosiC','475333');
# insert into users (email, FirstName,LastName,Nickname, password_) VALUES
# ('li90@gmail.com', 'li', 'coren','lico','231111');
# insert into users (email, FirstName,LastName,Nickname, password_) VALUES
# ('idor@gmail.com', 'ido', 'dor','idodo','222444');
# insert into users (email, FirstName,LastName,Nickname, password_) VALUES
# ('sati@gmail.com', 'neta', 'meir','dubi','234235');
# insert into users (email, FirstName,LastName,Nickname, password_) VALUES
# ('noami@gmail.com', 'noam', 'elli','noami','123456');

#users_partc -insert query
# insert into users_partc values ('1','noam','elli','12312')
# insert into users_partc values ('2','ido','cohen','324234')
# insert into users_partc values ('3','neta','meir','234234')
# insert into users_partc values ('4','shay','cohen','23423')
# insert into users_partc values ('5','noam','omer','2423')