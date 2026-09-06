# quotes_app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


from settings import Config


env_config = Config()
app.config['SECRET_KEY'] = env_config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = env_config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорты модулей приложения — САМЫМИ ПОСЛЕДНИМИ!
from . import models, forms, views, error_handlers, cli_commands


if __name__ == '__main__':
    app.run()
