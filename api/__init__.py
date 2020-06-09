from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    from .views import main 
    app.register_blueprint(main)

    return app



# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# # from flask_marshmallow import Marshmallow
# import os

# # Init app
# app = Flask(__name__)


# def create_app():
#     app = Flask(__name__)

#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#     db.init_app(app)

#     from .views import main
#     app.register_blueprint(main)

#     return app


# # @app.route()
# # Run Server
# if __name__ == '__main__':
#     app.run(debug=True)
