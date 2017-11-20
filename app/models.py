import datetime, re

from app import db

# make function that make nice looking url by replacing sapces with '-'
def slugify(s):
	return re.sub('[^\w]+', '-', s).lower

# make class of Entry model. it is subcalss from (db.Model)
class Entry(db.Model):
	
	# define columns of Entry table model
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	slug = db.Column(db.String(100), unique=True)
	body = db.Column(db.Text)
	created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
	modified_timestamp = db.Column(db.DateTime,default=datetime.datetime.now,onupdate=datetime.datetime.now)

	# Now start initializing the Entry Class after definiing the tables.
	def __init__(self, *args, **kwargs):
		# call parent class constructor, overridden the constructor for the class
		super(Entry, self).__init__(*args, **kwargs)
	
	# define function to make url slug
	def generate_slug(self):
		self.slug = ''
		if self.title:
			self.slug = slugify(self.title)
	
	# generate a helpful representation of instances of our Entry class. For Debugging
	def __repr__(self):
		return '<Entry: %s>' % self.title

