#should improt both app and views
from app import app, db # db is after making databse Entry model
import views

# after making databse Entry model:
import models


if __name__ == '__main__':
	app.run()