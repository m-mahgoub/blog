from app import app
from flask import render_template, request # for tempplate rendering


# 1st Chapters
# @app.route('/')
# def homepage():
# 	return 'Home Page'


# From Templates chapter
# simple without rendering
# @app.route('/')
# def homepage():
# 	return render_template('homepage.html')

@app.route('/')
def homepage():
	name = request.args.get('name') # 1st name is variable used inside the function, 2nd name represent a value passed in the url arguments for a variable called name
	number = request.args.get('number') # same as name
	# if not name:
	# 	name = '<unknown>' # can be replace by conditional inside jinja
	return render_template('homepage.html', name=name, number=number) # name and number arguments here represent a variable to be rendered inside jinja html file