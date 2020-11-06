import os

class base(object):
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.environ['SECRET_KEY']

class test(base):
	TESTING = True
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
	WTF_CSRF_ENABLED = False

class demo(base):
	DEBUG = True

class final(base):
	DEBUG = False