# make config object
import os # This is to get Directory for working app

### config object
class Configuration(object):
	DEBUG = True
    
### Database settings   

    # Define the directroy in which the module in located, for subsequent use
	APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
	
	# Defien database URI
	SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
	# avid the error message "SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning ""
	SQLALCHEMY_TRACK_MODIFICATIONS = False
