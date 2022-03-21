from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="faveo-handler",
    version="0.3.0",
    author="James Whale",
    author_email="james@james-whale.com",
    description="A Python library to interact with the Faveo API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WhaleJ84/faveo_handler",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.8',
    install_requires=[
        "requests",
    ],
)
