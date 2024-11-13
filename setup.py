from setuptools import  setup, find_packages

setup(
    name='mypackages',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Alx example of python packages',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/caleb-amenku/My_first_py_package.git',
    author='Caleb Amenku',
    author_email='calamenku1415@gmail.com'

)