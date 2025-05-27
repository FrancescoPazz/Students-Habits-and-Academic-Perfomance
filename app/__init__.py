from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7b181b6514f91c0ea9be84705df229b2fce0f0b97e6b36dd'

    from .routes import main
    app.register_blueprint(main)

    return app
