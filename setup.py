from setuptools import setup, find_packages

setup(
    name="face_sr",
    version="0.1",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[
        "torch"
    ],
)
