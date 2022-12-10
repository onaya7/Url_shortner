import os 
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# directory path
basedir = os.path.abspath(os.path.dirname(__file__))

# local sqlite database config
SQLALCHEMY_DATABASE_URI  ="sqlite:///" + os.path.join(
    basedir, "db.sqlite3"
)
SQLALCHEMY_TRACK_MODIFICATIONS  = False

