from setuptools import find_packages, setup  # Tools to create an installable package
from typing import List  # Allows us to add type hints (e.g., List[str])

# Variable to hold '-e .', which triggers setup.py from requirements.txt
# We save it here to easily find and remove it later so it doesn't cause errors.
HYPEN_E_DOT = "-e ."

def get_requirement(file_path: str) -> List[str]:
    '''
    Takes a file path, reads the file, and returns a clean list of libraries to install.
    '''
    requirements = []  # Empty list to store our library names
    
    with open(file_path) as file_obj:  # Open the requirements.txt file
        requirements = file_obj.readlines()  # Read all lines into our list
        
        # Loop through the list and remove invisible "new line" (\n) characters
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Check if '-e .' is in our list and remove it if it is
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements  # Return the clean list of libraries

# The main engine that sets up the project
setup(
    name="generic-ml-template", # Project name
    version="0.1.0",            # Project version
    description="Generic data science and machine learning starter project",
    author="Mohammed Hamid",
    author_email="mohammadhamid8554@gmail.com",
    
    # Tells setup to look inside the 'src' folder for our actual project code
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    # Runs our custom function to dynamically read libraries from requirements.txt
    install_requires=get_requirement("requirements.txt") 
)
