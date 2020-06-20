from functools import wraps
from flask import abort
from flask_jwt_extended import jwt_required


def admin(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        if not get_jwt_identity() == "admin":
            abort(403)
        
        return fn(*args, **kwargs)
    return wrapper