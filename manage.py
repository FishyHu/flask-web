from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from project import app, db
import os
import unittest
import coverage

app.config.from_object(os.environ['SETTINGS'])

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

@manager.command
def test():
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def cov():
	cov = coverage.coverage(branch=True,include='project/*')
	cov.start()
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)
	cov.stop()
	cov.save()
	cov.report()
	basedir = os.path.abspath(os.path.dirname(__file__))
	covdir = os.path.join(basedir,'coverage')
	cov.html_report(directory=covdir)
	cov.erase()

if __name__ == '__main__':
	manager.run()