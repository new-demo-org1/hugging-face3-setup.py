from setuptools import setup, find_packages

setup(
    name='example_package',
    version='1.0.0',
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        'xlm-roberta-large==1.2',
        '007J/smile',
        'xlnet-base-cased',
        'xlnet-large-cased'
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
