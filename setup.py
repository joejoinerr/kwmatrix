from pathlib import Path
from setuptools import setup

HERE = Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='kwmatrix',
    version='1.0.1',
    description='Combine keywords with several modifiers for SEO',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/joejoinerr/kwmatrix',
    author='Joe Joiner',
    author_email='joe@legato.digital',
    license='GPL',
    include_package_data=True,
    packages=['kwmatrix']
)
