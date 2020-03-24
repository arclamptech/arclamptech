from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import arclamptech
    app.register_blueprint(arclamptech.bp)

    return app