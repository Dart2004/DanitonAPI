import setuptools

with open("CHANGES.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="danitonapi-daniton999",
    version="0.0.1",
    author="Daniton999",
    author_email="zombieservers123@gmail.com",
    description="A global Artificial Intelligence Network called Daniton",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dart2004/DanitonAPI",
    project_urls={
        "Bug Tracker": "https://github.com/Dart2004/DanitonAPI/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
