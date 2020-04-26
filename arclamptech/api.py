from flask import Blueprint

bp = Blueprint("api", __name__, subdomain="api")

@bp.route('/')
def api():
    return "api.arclamptech.org"