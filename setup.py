try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'discription': 'An activity tracker for everyday tasks on computer',
	'author': 'Anke Ge',
	'url':'URL',
	'download_url':'download_url',
	'author_email':'geanke12@gmail.com',
	'version':'0.1',
	'install_requires':[],
	'packages':['NAME'],
	'scripts':[],
	'name': 'activitytracker'
	}

setup(**config)

