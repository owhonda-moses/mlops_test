from setuptools import setup, find_packages
from typing import List

hyphen_e = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function reads the requirements file and returns a list of requirements
    '''
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [x.replace('\n','') for x in requirements] # remove the newline character

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)


setup(
    name='mlops_test',
    version='0.01',
    author='owhonda-moses',
    author_email='owhondamoses7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)