class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'root',
      'password': 'P@ssw0rd',
      'host': '127.0.0.1',
      'db_name': '<接続先データベース名>'
  })
  
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  SECRET_KEY = 'arcaeaveryverysecretkey'

Config = SystemConfig