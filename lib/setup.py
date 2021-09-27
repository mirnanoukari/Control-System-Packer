import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="symbolical_dynamics", 
    version="0.0.1",
    author="Simeon Nedelchev",
    author_email="simkaned@gmail.com",
    description="A package provide some routines on modeling mechanical systems",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
    ],
    packages=setuptools.find_packages(),
    # install_requires = ['']
    python_requires=">=3.6",
)