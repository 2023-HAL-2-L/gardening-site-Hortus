import uuid
import datetime


def generate_uuid():
    return str(uuid.uuid4())


def time_now():
    tz_jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(tz_jst)
