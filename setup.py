
from setuptools import setup, find_packages
__version__ = '0.1.0'


setup(
    name='starfighter',
    version=__version__,
    author='Brendan Abel',
    author_email='007brendan@gmail.com',
    packages=['starfighter'],
    package_dir={'starfighter': 'starfighter'},
    package_data={'starfighter': ['data/*.txt']},
)
