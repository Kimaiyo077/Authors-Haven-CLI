from setuptools import setup

setup(
    name= "authorsHavenCLI",
    version = "7.0",
    py_modules=['ah-cli'],
    install_requires=[
        'click', 'requests'
    ],
    entry_points={'console_scripts': ['ah = ah.commands:ah']},
)