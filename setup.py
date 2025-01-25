import setuptools
from distutils.core import setup

with open("README.md") as f:
    long_description = f.read()

with open("Supercluster/version.txt") as f:
    version = f.read().strip()

setup(
    name="Supercluster",
    version=version,
    description="A powerful and flexible AI agent framework in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "ai",
        "agent",
        "framework",
        "machine learning",
        "artificial intelligence",
    ],
    author="Supercluster-dev",
    author_email="dev@Supercluster.ai",
    packages=setuptools.find_packages(),
    package_data={"Supercluster": ["version.txt"]},
    install_requires=[
        "requests==2.31.0",
        "rich==13.9.4"
    ],
    dependency_links=[],
    python_requires=">=3.10",
    url="https://Supercluster.github.io/",
    entry_points={
        'console_scripts': ['Supercluster=Supercluster.__main__:main']
    }
)
