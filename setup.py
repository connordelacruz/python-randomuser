from setuptools import setup, find_packages

# Get __version__
with open('./randomuser/version.py') as f:
    exec(f.read())

setup(name='randomuser',
      version=__version__,
      description='Python class for generating random user data using https://randomuser.me API',
      url='http://connordelacruz.com/python-randomuser/',
      download_url='https://github.com/connordelacruz/python-randomuser/archive/{}.tar.gz'.format(__version__),
      author='Connor de la Cruz',
      author_email='connor.c.delacruz@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
