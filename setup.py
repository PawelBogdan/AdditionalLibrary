import setuptools

setuptools.setup(
    name="Additional Library",
    version="1.0",
    author="Paweł Bogdan",
    author_email="pawel.bogdan1@gmail.com",
    description="Some example library to import in the other project",
    url="https://github.com/PawelBogdan/AdditionalLibrary",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
