from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["numpy"],
    url="https://github.com/FrancisGengarh/mypackage",
    author="FrancisGengarh",
    author_email="onyangofrancis23@gmail.com"
)
