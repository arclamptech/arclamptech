from flask import (
    Blueprint, render_template, request
)
from flask import jsonify

bp = Blueprint("arclamp", __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/resources/')
def resources():
    return render_template('resources.html')

@bp.route('/reveal')
def reval():
    return jsonify({'ip': request.remote_addr}), 200