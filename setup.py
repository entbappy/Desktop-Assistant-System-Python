from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Neuron-Desktop-Assistant"
AUTHOR_USER_NAME = "iNeuron-Pvt-Ltd"
SRC_REPO = "desktop_entity_layer"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="BOKTIAR AHMED BAPPY",
    description="A small package for Neuron-Desktop-Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="boktiar@ineuron.ai",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)