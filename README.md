## nitropy a simple game development libary for Python.

### Features
- custom window resolution
- custom window title
- more coming soon.

### Needs
- Python 3.6 or higher
- Windows 10 or higher

## Setup
### Step 1
Open a command prompt window on the root of the library and run the following command:
```shell
python setup.py build --build-lib nitropy_lib_build
```
This should build the library and create a folder named nitropy_lib_build
### Step 2
Open a command prompt window again on the root of the library and run the following command:
```shell
python setup.py sdist bdist_wheel
```
This should install the needed files.
### Step 3
Run the following command to clean up the folders and move the to the nitropy_lib_build folder: (adjust to your domain)
```shell
Move-Item -Path "build" -Destination "nitropy_lib_build/"
Move-Item -Path "dist" -Destination "nitropy_lib_build/"
Move-Item -Path "nitropy.egg-info" -Destination "nitropy_lib_build/"
```
this should move all the build folders to the nitropy_lib_build folder to clean up.
### Step 4
Run the following command to install all packages:
```shell
pip install nitropy_lib_build/dist/nitropy_lib-0.1-py3-none-any.whl
```
after this you are done and you can try programming some games with nitropy. examples can be found in the releases tab.
## How to update the library
### Step 1
Run the following command:
```shell
python setup.py sdist bdist_wheel


```
This should reinstall the needed files.

After this run the following command to clean the build files up and move them to nitropy_lib_build
```shell
if (Test-Path -Path "nitropy_lib_build/build") {
    Remove-Item -Recurse -Force "nitropy_lib_build/build"
}

if (Test-Path -Path "nitropy_lib_build/dist") {
    Remove-Item -Recurse -Force "nitropy_lib_build/dist"
}

if (Test-Path -Path "nitropy_lib_build/nitropy.egg-info") {
    Remove-Item -Recurse -Force "nitropy_lib_build/nitropy_lib.egg-info"
}

Move-Item -Path "build" -Destination "nitropy_lib_build/"
Move-Item -Path "dist" -Destination "nitropy_lib_build/"
Move-Item -Path "nitropy_lib.egg-info" -Destination "nitropy_lib_build/"

```
### Step 2
Run the following command to uninstall nitropy:
```shell
pip uninstall nitropy


```
After this run the following command to reinstall nitropy again:
```shell
pip install nitropy_lib_build\dist\nitropy_lib-0.2-py3-none-any.whl


```
After this you are done and the library is updated.
