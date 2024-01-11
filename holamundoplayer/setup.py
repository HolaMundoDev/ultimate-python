import setuptools
from pathlib import Path

long_desc = Path("README.md").read_text()
setuptools.setup(
    name="holamundoplayer",
    version="0.0.1",
    long_description=long_desc,
    packages=setuptools.find_packages(exclude=["mocks,tests"])
)