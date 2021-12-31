# from os import environ


# class Config:
#     '''
#     The default configuration object for the app.
#     '''
#     AWS_REGION = environ.get('AWS_REGION', 'us-west-2')
#     AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID', 'AKIAIOSFODNN7EXAMPLE')
#     AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET', 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY')
#     AWS_DEFAULT_OUTPUT = environ.get('AWS_DEFAULT_OUTPUT', 'json')

class Config(object):
    """ 
	Common Configuration
	"""
    pass

class DevelopmentConfig(Config):
	"""
	Configuration for development environment
	"""
	DEBUG = True

class ProductionConfig(Config):
	"""
	Configuration for development environment
	"""
	DEBUG = False

app_config = {
	'development' : DevelopmentConfig,
	'production' : ProductionConfig
}

    
    