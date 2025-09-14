from setuptools import setup, find_packages

setup(
    name="gpg-authinfo",
    version="0.1.0",
    author="Your Name",
    author_email="gopeterjun@naver.com",
    description="A helper module to read GPG-encrypted authinfo files for API credentials",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "python-gnupg",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires=">=3.6",
)