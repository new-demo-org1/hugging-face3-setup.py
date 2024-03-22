from setuptools import setup, find_packages

setup(
    name='example_package',
    version='1.0.0',
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        "xlm-roberta-large==4.13.0",
        "jonatasgrosman/wav2vec2-large-xlsr-53-english",
        "openai/clip-vit-large-patch14",
        "microsoft/resnet-50",
        "stabilityai/stable-diffusion-xl-base-1.0",
        "stabilityai/stable-diffusion-xl-refiner-1.0",
        "cl-tohoku/bert-base-japanese",
        "openai/clip-vit-base-patch32",
        "dslim/bert-base-NER",
        "neuralmind/bert-base-portuguese-cased"
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
