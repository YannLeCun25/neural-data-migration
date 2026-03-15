from setuptools import setup, find_packages

setup(
    name="neural-data-migration",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    author="Yann LeCun",
    description="High-performance ETL pipeline for high-dimensional neural network datasets.",
    url="https://github.com/YannLeCun25/neural-data-migration",
)
