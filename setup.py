from setuptools import setup

setup(
    name="Package_example1", # Replace with your own username
    version="0.0.1",
    author="GabrielBlancoMora",
    author_email="gaboblanco256@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GabrielBlancoM/Tarea3.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'playsound',
        'opencv-python',
        'matplotlib',
        ],
    package_dir=Package_example1:Package_example2,
    scripts=['Package_example2/images', 'Package_example2/sonido', 'Package_example2/text']
) 