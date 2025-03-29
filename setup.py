from setuptools import setup, find_packages

setup(
    name="vat",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "scikit-learn",
        "scipy"
    ],
)