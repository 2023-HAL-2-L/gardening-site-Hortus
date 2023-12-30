import uuid
import datetime


def generate_uuid():
    return str(uuid.uuid4())


def time_now():
    return datetime.timezone(datetime.timedelta(hours=9))
