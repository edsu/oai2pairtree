from setuptools import setup

setup(
    name = 'oai2pairtree',
    version = '0.0.1',
    url = 'http://github.com/edsu/oai2pairtree',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    py_modules = ['oai2pairtree',],
    scripts = ['oai2pairtree.py'],
    platforms = ['POSIX'],
    install_requires = ['lxml', 'ptree']
)
