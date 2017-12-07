import datetime, re

from app import db

# make function that make nice looking url by replacing sapces with '-'
def slugify(s):
	return re.sub('[^\w]+', '-', s).lower

#$$$$$$$$$$$ Belong to Relational system
## Make Table called entry_tags with two columns refer to id of tag and entery
entry_tags = db.Table ('entry_tags',
	db.Column ('tag_id', db.Integer, db.ForeignKey('tag.id')),
	db.Column ('entry_id', db.Integer, db.ForeignKey('entry.id')))
#$$$$$$$$$$$

# make class of Entry model. it is subcalss from (db.Model)
class Entry(db.Model):
	
	# define columns of Entry table model
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	slug = db.Column(db.String(100), unique=True)
	body = db.Column(db.Text)
	created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
	modified_timestamp = db.Column(db.DateTime,default=datetime.datetime.now,onupdate=datetime.datetime.now)

	#$$$$$$$$$$$ Belong to Relational system
	## Setting the tags attribute of the Entry class equal to the return value of the db.relationship function
	tags = db.relationship(
		'Tag',
		secondary=entry_tags,
		backref= db.backref('entries', lazy='dynamic')
		)

	'''
	The first two arguments, 'Tag' and secondary=entry_tags, instruct SQLAlchemy that we are going to be querying the Tag model via the entry_tags table. The third argument creates a back-reference, allowing us to go from the Tag model back to the associated list of blog entries. By specifying lazy='dynamic', we instruct SQLAlchemy that, instead of it loading all the associated entries for us, we want a Query object instead
	'''
	
	#$$$$$$$$$$$

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

########################## Relational system
#### From Bulding Tagging system: Also Above in the lines beween between #$$$$$$$$$$$ and #$$$$$$$$$$$

# make db for Tags
class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	slug = db.Column(db.String(64) , unique=True)

def __init__(self, *args, **kwargs):
	super(Tag, self).__init__(*args, **kwargs)
	self.slug = slugify(self.name)

def __repr__(self):
		return '<Tag: %s>' % self.name