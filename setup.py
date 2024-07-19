from setuptools import setup, find_packages

setup(
    name='nitropy',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pygame',
    ],
    description='a simple game development library for Python.',
    author='cornedev',
    author_email='corneproductions@gmail.com',
    url='https://github.com/cornedev/nitropy_lib',  # replace with your actual repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
