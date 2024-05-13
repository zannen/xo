import setuptools

VERSION = "0.0.1"

setuptools.setup(
    name="xo",
    version=VERSION,
    author="ZanNen",
    author_email="",
    description="A Naughts and Crosses game",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/zannen/xo",
    packages=setuptools.find_packages(),
    package_data={"xo": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[],
    setup_requires=["wheel"],
    zip_safe=False,
)
