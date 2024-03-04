import uuid
import datetime
from flask import Flask

def generate_uuid():
    return str(uuid.uuid4())


def time_now():
    tz_jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(tz_jst)

def prepare_response(data):
    response = Flask.make_response(data)
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = 'default-src \'self\''
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    # response.headers['X-XSS-Protection'] = '1; mode=block'
    return response