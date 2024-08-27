#!/usr/bin/env python3
"""flask app"""

from flask import Flask, render_template
from flask_babel import Babel, request


app = Flask(__name__)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
