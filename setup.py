try:
    from setuptools import setup
except ImportError:
    from distutils import setup
    
setup(
      name='MongoDict',
      version='0.0.1',
      description='',
      author='Shane R. Spencer',
      author_email='shane@bogomip.com',
      url='https://github.com/whardier/MongoDict',
      packages=['mongodict'],
      install_requires=['pymongo']
)
