from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

# Get __version__
with open('randomuser.py') as f:
    exec(f.read())

setup(name='randomuser',
      version=__version__,
      description='Python class for generating random user data using https://randomuser.me API',
      long_description=readme(),
      url='http://connordelacruz.com/python-randomuser/',
      download_url='https://github.com/connordelacruz/python-randomuser/archive/{}.tar.gz'.format(__version__),
      author='Connor de la Cruz',
      author_email='connor.c.delacruz@gmail.com',
      license='MIT',
      py_modules=['randomuser'],
      zip_safe=False)
