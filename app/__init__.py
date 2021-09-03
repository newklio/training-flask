import re
from flask import Flask, render_template, request
from werkzeug.utils import redirect

def create_app():
    app = Flask(__name__)
    
    creds  = {
        "yogesh":"pass1234",
        "Rica":"rica12345"
    }

    @app.route('/<string:name>')
    def root(name):
        return render_template('main.html', name=name)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():

        if request.method == 'POST':
            data = request.form
            username = data['username']
            password = data['pass']

            print(username, password)
            if username in creds.keys():
                if password == creds[username]:
                    return f"{username} logged in successfully"
                else:
                    return "password wrong"
            return "username or password not matched with our database"

        else:
            print(request.method)
            return render_template('entrance/login.html')



    @app.route('/signup/<string:name>')
    def singup(name):
        return name
    return app