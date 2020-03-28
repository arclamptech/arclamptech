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
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return jsonify({'ip': ip}), 200