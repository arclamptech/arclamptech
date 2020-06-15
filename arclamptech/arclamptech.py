from flask import (
    Blueprint, render_template, request
)
from flask import jsonify

bp = Blueprint("arclamp", __name__, subdomain='www')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/resources/')
def resources():
    return render_template('resources.html')