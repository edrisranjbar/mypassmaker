import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypassmaker",
    version="1.5",
    author="Edris Ranjbar",
    license='MIT',
    packages=['mypassmaker'],
    author_email="edris.qeshm2@gmail.com",
    description="A secure password and passphrase generator with safety evaluation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edrisranjbar/mypassmaker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)