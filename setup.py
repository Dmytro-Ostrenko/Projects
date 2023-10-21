from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.1',
    author='Dmytro Ostrenko',
    author_email='dmytro.ost1@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:start']}
)