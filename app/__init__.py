from os import removedirs
from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    creds = {
        "yogesh": "pass1234",
        "Rica": "rica12345"
    }

    @app.route('/')
    def index():
        return render_template('main.html', title="Dashboard")

    @app.route('/view')
    def view():
        return render_template('views/views.html')

    @app.route('/settings')
    def settings():
        return render_template('settings/settings.html', names=['settigs', 'profile', 'dashboard', 'yogesh', 'views'])

    return app
