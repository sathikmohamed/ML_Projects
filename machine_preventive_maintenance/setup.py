from setuptools import find_packages,setup
from typing import List

hypen_e="-e ."

def get_requirements(filepath:str)->List[str]:     
    """this function will return the list of requirements """
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        if hypen_e in requirements:
            requirements.remove(hypen_e)

    return requirements


setup( 
  name="Machine predective maintenace",
  version='0.0.01',
  packages=find_packages(),
  author="sathik",
  install_requires=get_requirements("requirements.txt")
)
