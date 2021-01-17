from setuptools import setup

setup(
    name='Topy',
    version='0.1.0',
    packages=['topy'],
    entry_points={
        'console_scripts': [
            'topy = topy.__main__:main'
        ]
    })
