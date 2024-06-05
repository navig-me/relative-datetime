from setuptools import setup, find_packages

setup(
    name='relative-datetime',
    version='0.1.3',
    description='A Python library to get relative datetime strings and parse datetime strings.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mihir Khandekar',
    author_email='mihirkhandekar@gmail.com',
    url='https://github.com/mihirkhandekar/relative-datetime',
    packages=find_packages(),
    install_requires=[
        'python-dateutil',
        'pytz',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
