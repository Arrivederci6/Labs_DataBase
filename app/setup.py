from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_back',
    version='0.0',
    description='Flask back - lab 4',
    author='<Morozov Andrii>',
    author_email='<tba>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
