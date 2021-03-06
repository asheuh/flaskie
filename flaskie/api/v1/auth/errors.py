import re
from flaskie.database import db, requestsdb
from flaskie.api.restplus import api

def user_is_valid(data):
    """user error handling"""
    from .collections import store

    errors = {}
    if store.get_by_field(key='email', value=data.get('email')) is not None:
        errors['email'] = "The email you provided is in use by another user"
    if store.get_by_field(key='username', value=data.get('username')) is not None:
        errors['username'] = "The username you provided already exists"
        
    return errors

def abort_if_doesnt_exists(user_id):
    """Checks if given id exists in the database"""
    if user_id not in db:
        api.abort(404, "User with id {} doesn't exist or your provided an id that does not belong to you".format(user_id))

def abort_if_request_doesnt_exists(id):
    """Checks if given id exists in the database"""
    if id not in requestsdb:
        api.abort(404, "Request with id {} doesn't exist".format(id))

def check_valid_email(email):
    """Checks if the email provided is valid"""
    return re.match(r'^.+@([?)[a-zA-Z0-9-.])+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$', email)