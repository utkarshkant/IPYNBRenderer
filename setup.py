import setuptools 

# open readme file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"               # specify version number

REPO_NAME = "IPYNBRenderer"         # define repository name
AUTHOR_USER_NAME = "utkarshkant"    # declare my username
AUTHOR_EMAIL = "utkarsh.kant@gmail.com"    # declare my email
SRC_REPO = "TPYNBRenderer"          # define source repository name

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for file rendering in Jupyter notebook",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"", "src"},
    packages=setuptools.find_packages(where='src'),
)