from setuptools import setup

install_requires = ['libtcod-cffi', 'pygame']
tests_require = []

setup(
    name='pabloquest3',
    version='0.0.1',
    description="RPG Game",
    author='Pablo Sarmiento',
    url="pabloquest.wikispaces.com",
    author_email='cebollinos@gmail.com',
    copyright = "Copyright (c) 2012 Pablo Sarmiento.",
    packages=['pabloquest'],
    install_requires=install_requires,
)
