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


app.config.from_object(Config)
# app.config['users'] = Config.users
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get_user"""
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """Set the user before processing each request"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages"""
    user = getattr(g, 'user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
