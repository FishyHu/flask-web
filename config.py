import os

class base(object):
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.environ['SECRET_KEY']

class demo(base):
	DEBUG = True

class final(base):
	DEBUG = False