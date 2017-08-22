from setuptools import setup, find_packages 

setup(
    name='damndaily',
    packages=find_packages(),
    version='0.1',
    license='MIT',
    author_email='nils@hindenbug.de',
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy'
    ]
)
