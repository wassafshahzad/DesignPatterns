import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="design-patterns-Wassaf-Shahzad", # Replace with your own username
    version="0.0.1",
    author="Wassaf Shahzad",
    author_email="wassafshahzad@gmail.com",
    description="A small python module containing decorators for implementing design patterns",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wassafshahzad/DesignPatterns.git",
    packages=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3',
)