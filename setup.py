from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirement:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='Diamond Price Prediction',
    version='0.0.1',
    author='Babita',
    author_email='babitapatwal2000@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
