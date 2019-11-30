from setuptools import setup, find_packages
import phonebook

setup(
    name='Phonebook',
    description='Simple phone book',
    version=phonebook.__version__,
    author=phonebook.__author__,
    author_email=phonebook.__email__,
    packages=find_packages(),
    package_data={
        'phonebook': ['*']
    },
    install_requires=['npyscreen>=4.10.5'],
    entry_points={
            'console_scripts': [
                'phonebook = phonebook.phonebook:main',
            ]
    },
)

