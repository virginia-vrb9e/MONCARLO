from setuptools import setup, find_packages

setup(
    name='moncarlo',
    version='1.0.0',
    url='https://github.com/virginia-vrb9e/DS5100-project-repo',
    author='Virginia Brame',
    author_email='vrb9e@virginia.edu',
    description='This is the moncarlo package.  It allows a user to create Monte Carlo simulation devices, engage in various levels of play, and collect statistics about the devices and the plays.',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    license='LICENSE.txt'
)
