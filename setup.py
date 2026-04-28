from setuptools import setup, find_packages

setup(
    name="datascience_folder_structure",
    version="0.2.0",
    description="Add your description here",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    packages=find_packages(where="."),
    package_dir={"": "."},
    package_data={
        "dspackagefolder": ["template/**"],
    },
    install_requires=[
        "path>=17.1.1",
        "python-dotenv>=1.2.1",
        "sqlalchemy>=2.0.48",
        "toml>=0.10.2",
    ],
    entry_points={
        "console_scripts": [
            "createdatasciencefolder=dspackagefolder.main:create_ds_folder_cli",
        ],
    },
    include_package_data=True,
)
