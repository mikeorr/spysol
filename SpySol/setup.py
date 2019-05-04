import setuptools

def readme():
    with open("README.rst") as f:
        return f.read()

REQUIRES  =  [
    "reprutils",
    ]

setuptools.setup(
    name = "SpySol",
    version = "0.0",
    description = "A Spider solitaire game.",
    #long_description = readme()
    classifiers = [
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: Esperanto",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Games/Entertainment :: Puzzle Games",
        ],
    keywords = "spider solitaire card game",
    url = "https://github.com/mikeorr/spysol",
    author = "Mike Orr",
    author_email = "sluggoster@gmail.com",
    license = "MIT",
    packages = ["spysol"],
    install_requires = REQUIRES,
    #tests_require = ["pytest"],
    #setup_requires = ["pytest-runner"],
    extras_require = {
        "tests": ["pytest"],
        },
    zip_safe = False,
    )
