import os

class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="dse",
        password="Ap4tW!veyHp35nM5",
        hostname="dse.mysql.pythonanywhere-services.com",
        databasename="dse$fma",
    )
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False
