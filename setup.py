from setuptools import setup, find_packages

setup(
    name='example_package',
    version='1.0.0',
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        "xlm-roberta-large==4.13.0",
        "09panesara/distilbert-base-uncased-finetuned-cola",
        "xlnet-base-cased",
        "xlnet-large-cased",
        "007J/smile==1.235.dd",
        "0307061430/xuangou",
        "0x7194633/keyt5-base",
        "0x7194633/keyt5-large",
        "0xDEADBEA7/DialoGPT-small-rick",
        "123123/ghfk"
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
