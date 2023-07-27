from setuptools import setup, PEP420PackageFinder

setup(
    name='foo',
    version="1.0.0",
    packages=PEP420PackageFinder.find(),
    package_data={
        '': ['*.pyd', '*.so']
    }
)
