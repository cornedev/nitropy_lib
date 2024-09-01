from setuptools import setup, find_packages

setup(
    name='nitropy_lib',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pygame',
    ],
    description='a simple library base for Python',
    author='yourname',
    author_email='youremail',
    url='https://github.com/cornedev/nitropy_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires= '>=3.6',
)