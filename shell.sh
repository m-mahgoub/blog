# chapter 1

cd /home/mohamed/Desktop/blog/blog

virtualenv blog

source bin/activate  # Python 2.7.12


pip install Flask

mkdir app

touch app/{__init__,app,config,main,views}.py

python main.py

# chapter 2
pip install SQLAlchemy

pip install flask-sqlalchemy


touch models.py

mkdir scripts

touch scripts/create_db.py

python scripts/create_db.py

pip install ipython

ipython

# rerun script after making tag system
python scripts/create_db.py

pip install flask-migrate

touch manage.py

