from setuptools import setup
import mycommon

VERSION = mycommon.__version__

PACKAGES = [
 'mycommon'
]
setup(
    name='mycommon',
    version=VERSION,
    packages=PACKAGES,
)