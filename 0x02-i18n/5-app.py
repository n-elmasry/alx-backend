#!/usr/bin/env python3
"""flask app"""

from flask import Flask, render_template, g
from flask_babel import Babel, request


app = Flask(__name__)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


app.config.from_object(Config)
app.config['users'] = Config.users
babel = Babel(app)


def get_user():
    """get_user"""
    user_id = request.args.get('login_as', type=int)
    if user_id is None:
        return None
    return app.config['users'].get(user_id)


@app.before_request
def before_request():
    """Set the user before processing each request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
