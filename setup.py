# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")



setup(
  
    name = "learn-chinese",
   
    version="2.0.0", 
    
    description="On Screen Translator - Chinese Learning Assistance Tool",  
   
    long_description=long_description,  
    
    author="Conner Sommerfield",  
    
    packages=find_packages(where="learn-chinese"),  
    
    python_requires=">=3.7, <4",
    
)