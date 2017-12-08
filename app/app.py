from flask import Flask # 1st
# %%%%%%%%%%%%%%
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# %%%%%%%%%%%%%%
from flask_sqlalchemy import SQLAlchemy # 2nd
from config import Configuration # 1st



# make flask app
app = Flask(__name__)

# use configuration from config file
app.config.from_object(Configuration)

# Create an object called "db" that will manage databse connection between flask app and databse file
db = SQLAlchemy(app)
# %%%%%%%%%%%%%%
migrate = Migrate(app, db)
# %%%%%%%%%%%%%%

# %%%%%%%%%%%%%%
manager = Manager(app)
manager.add_command('db', MigrateCommand)
# %%%%%%%%%%%%%%





'''
Chapters identifiers:
Databases: Migration = # %%%%%%%%%%%%%%

'''
