import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "graphvizcyberrenderer",
    version = "0.1",
    author = "Me",
    author_email = "bruno.m.voss@gmail.com",
    description = ("using graphviz to render my cybernetic systems"),
    
    license = "I don't license this. If you have it, delete it.",
    keywords = ["cyber","graphviz",],
   
    packages=['graphviz_cyber'],
    
)
