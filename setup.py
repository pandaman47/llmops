from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    Returns a list of requirements for the project
    """

    req_list:List[str] = []

    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()  #remove any spaces or indents
                if line and not line.startswith("#") and line != '-e .':
                    req_list.append(line)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return req_list

setup(
    name="travel_planner",
    version='0.0.1',
    author='saketh',
    packages=find_packages(),
    install_requires=get_requirements(),
)
