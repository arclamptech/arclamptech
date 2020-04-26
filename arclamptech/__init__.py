from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.config['SERVER_NAME'] = 'arclamptech.org'

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import arclamptech
    app.register_blueprint(arclamptech.bp)

    from . import api
    app.register_blueprint(api.bp)

    return app