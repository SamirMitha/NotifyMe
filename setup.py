import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'pypi.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="notifyme_traveltimer",
    version="1.0.1",
    license="MIT",
    author="Samir Mitha, Dumitru Cotorobai",
    author_email="samir.mitha@gmail.ca",
    description="Functions for use with end to end travel and wait timing.",
    long_descriptio=long_description,
    url = "https://github.com/SamirMitha/NotifyMe",
    packages=setuptools.find_packages(),
    install_requires = [
        'googlemaps',
        'pyowm',
        'tweepy',
        'pandas'
    ],
    python_requires=">=3.8",
)