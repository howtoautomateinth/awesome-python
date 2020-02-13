import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-hta-helloworld", 
    version="0.0.3",
    author="Howtoautomate.in.th",
    author_email="mart@howtoautomate.in.th",
    description="A hellowold example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/howtoautomateinth/awesome-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)