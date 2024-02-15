from setuptools import setup, find_packages

setup(
    name='example_package',
    version='1.0.0',
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        "0x7194633/keyt5-base==4.13.0",
        "0307061430/xuangou",
        "Salesforce/ctrl",
        "007J/smile==1.235.dd",
        "albert-base-v1"
    ],
    author='Your Name',
    author_email='your@email.com',
    description='A short description of your package',
    url='https://github.com/yourusername/example_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
