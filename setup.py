# python setup.py bdist_wheel
#!/usr/bin/env python

from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
    "pillow",
    "tqdm",
    "numpy",
    "scikit-image",
    "opencv-python"
]

setup(name='synthetic-data',
      version='0.0.1',
      description='This Package handles tools for generating synthetic data',
      author='Friedrich Muenke',
      author_email='friedrich.muenke@me.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=REQUIRED_PACKAGES,)
