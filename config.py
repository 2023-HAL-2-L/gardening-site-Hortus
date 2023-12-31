import os
class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'root',
      'password': 'Passw0rd',
      'host': '127.0.0.1',
      'db_name': 'IH'
  })
  
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  WTF_CSRF_ENABLED = True
  FLASK_ENV="development"
  SECRET_KEY = os.urandom(24)
  SQLALCHEMY_TRACK_MODIFICATIONS = False

Config = SystemConfig