from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function reads the requirements.txt file and returns a list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        [req.replace("\n","")for req in requirements]
    
        if  HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='Emre Dost',
    author_email= 'emredost1987@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    )