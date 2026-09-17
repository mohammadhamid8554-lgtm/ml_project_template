from setuptools import find_packages, setup

setup(
    name="generic-ml-template",
    version="0.1.0",
    description="Generic data science and machine learning starter project",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "pytest",
        "python-dotenv",
    ],
)
