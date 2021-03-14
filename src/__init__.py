from flask import Flask

from .extensions import mongoDB
# init SQLAlchemy so we can use it later in our models


def create_app(config_object='src.settings'):
    app = Flask(__name__)

    app.config.from_object(config_object)

    mongoDB.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
