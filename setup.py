from setuptools import setup

setup(
    name="anarci",
    version="1.3",
    description="Antibody Numbering and Receptor ClassIfication",
    author="James Dunbar",
    author_email="opig@stats.ox.ac.uk",
    url="http://opig.stats.ox.ac.uk/webapps/ANARCI",
    packages=["anarci"],
    package_dir={"anarci": "lib/python/anarci"},
    package_data={"anarci": ["dat/HMMs/*"]},
    install_requires=["biopython"],
    scripts=["bin/ANARCI"],
)
