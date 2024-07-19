**nitropy a great game development libary for Python**
*in development by cornedev*

*nitropy setup guide:*

*setup:*
**run the following command to build the library:**

python setup.py build --build-lib nitropy_lib_build

**run the following command to install the needed files**

python setup.py sdist bdist_wheel

**run the following command to clean up the folders and move the to the build folder:** *(adjust to your domain)*

mv C:\Users\corne\OneDrive\Desktop\nitropy_lib\build C:\Users\corne\OneDrive\Desktop\nitropy_lib\dist C:\Users\corne\OneDrive\Desktop\nitropy_lib\nitropy_lib.egg-info C:\Users\corne\OneDrive\Desktop\nitropy_lib\nitropy_lib_build

**run the following command to install all packages:**

pip install nitropy_lib_build/dist/nitropy_lib-0.1-py3-none-any.whl

*after doing this you're done and can start programming with nitropy!*
