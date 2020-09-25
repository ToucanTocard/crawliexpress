import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crawliexpress",  # Replace with your own username
    version="0.0.1",
    author="ToucanTocard",
    author_email="contact@robin.ninja",
    description="Another Aliexpress Crawler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toucantocard/crawliexpress",
    packages=setuptools.find_packages(include=["crawliexpress"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.6",
    install_requires=["requests", "jsonnet", "bs4"],
    setup_requires=[],
    tests_require=[],
)
