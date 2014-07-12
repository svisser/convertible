from distutils.core import setup

setup(
    name='convertible',
    version='0.1',
    py_modules = ['convertible'],
    install_requires = ['jsonpickle'],
    description='Python library for converting object into dictionary/list structures and json',
    long_description='Python library for converting object into dictionary/list structures and json',
    license='GPLv2',
    author='Vladimir Sapronov',
    author_email='vladimir.sapronov@gmail.com',
    maintainer='Vladimir Sapronov',
    maintainer_email='vladimir.sapronov@gmail.com',
    url='https://github.com/syncloud/convertible')