import setuptools

setuptools.setup(
    name="notifyme",
    version="1.0.0",
    license="MIT",
    author="Samir Mitha, Dumitru Cotorobai",
    author_email="samir.mitha@gmail.ca",
    description="Functions for use real-time end to end travel and wait timing.",
    url = "https://github.com/SamirMitha/NotifyMe"
    packages=setuptools.find_packages(),
    install_requires = [
        'googlemaps',
        'pyowm',
        'tweepy',
        'pandas'
    ],
    python_requires=">=3.8",
)