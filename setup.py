from setuptools import setup, find_packages

setup(
    name="bitgate",
    version="v2024.08.30.2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
