from setuptools import setup, find_packages

setup(name='randomuser',
        version='0.3.1',
        description='Python class for generating random user data using https://randomuser.me API',
        url='http://connordelacruz.com/python-randomuser/',
        download_url='https://github.com/connordelacruz/python-randomuser/archive/0.3.1.tar.gz',
        author='Connor de la Cruz',
        author_email='connor.c.delacruz@gmail.com',
        license='MIT',
        packages=find_packages(),
        zip_safe=False)
