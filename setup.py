from setuptools import setup, find_packages

setup(
    name='yourlibraryname',
    version='0.3', #edit this when updating your library
    packages=find_packages(),
    install_requires=[
        'pygame',
    ],
    #change the install_requires based on the librarys needed for your library.
    description='a simple library base for Python',
    author='yourname',
    author_email='youremail',
    url='https://github.com/cornedev/nitropy_lib',
    #replace this with your repository for your library.
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires= '>=3.6',
)
