import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = "GxQ)(eF|lJ%/>)JEmrHR0tw=%N'5<+hdF+EpXTZNIF|XFF(eUPrgd3.Zv*w20?X"

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
