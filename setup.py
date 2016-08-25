from setuptools import setup, find_packages
try:
    from urllib import request
except ImportError:
    import urllib2 as request
fastep = request.urlopen('https://raw.githubusercontent.com/ninjaaron/fast-entry_points/master/fastentrypoints.py')
namespace = {}
exec(fastep.read(), namespace)

setup(
    name='ypm',
    version='0.0.1',
    description='yank and put files on the command line',
    long_description=open('README.rst').read(),
    url='https://github.com/ninjaaron/ypm',
    author='Aaron Christianson',
    author_email='ninjaaron@gmail.com',
    keywords='yank put move',
    py_modules = ['ypm'],
    classifiers=['Programming Language :: Python :: 3.5'],
    entry_points={'console_scripts': [
        'yank=ypm:yank',
        'put=ypm:put',
        'move=ypm:move'
        ]},
    )
