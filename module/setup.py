from setuptools import setup, find_packages

VERSION = 'v1.0'
DESCRIPTION = 'GifGang Python Module'
LONG_DESCRIPTION = 'Official Python Module by GifGang that wraps many APIs'

setup(
    # the name must match the folder name 'verysimplemodule'
    name="gifgang",
    version=VERSION,
    author="Hirusha Adikari",
    author_email="<zesta5j7k@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    keywords=['python', 'gifgang'],
    classifiers=[
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
