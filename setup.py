from distutils.core import setup

requirements = [
    'jsonpickle==0.7.1'
]

setup(
    name='convertible',
    version='0.2',
    py_modules = ['convertible'],
    install_requires = requirements,
    description='Python library for converting object into dictionary/list structures and json',
    long_description='Python library for converting object into dictionary/list structures and json',
    license='GPLv3',
    author='Vladimir Sapronov',
    author_email='vladimir.sapronov@gmail.com',
    maintainer='Vladimir Sapronov',
    maintainer_email='vladimir.sapronov@gmail.com',
    url='https://github.com/syncloud/convertible')