from setuptools import setup, find_packages

setup(
    name="LasyGen",
    version="0.1",
    author="Ilmo Salmenperä",
    author_email="ilmo.salmenpera@helsinki.fi",
    packages=find_packages(),
    url="http://github.com/MrCubanfrog/LasyGen",
    license = "LICENSE",
    description="A Small python program for generating a song book for academic table parties",
    install_requires=[
    ], 
    long_description=open("README.md").read(),
    entry_points='''
        [console_scripts]
        lasygen=lasygen:main
    ''',

)
