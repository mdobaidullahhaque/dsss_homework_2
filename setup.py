
from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # List dependencies here if any
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz'  # 'math_quiz' is the command to run
        ]
    },
    author="mdobaidullahhaque",
    author_email="mdobaidullahhaque.cse@gmail.com",
    description="math quiz homework 2",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mdobaidullahhaque/dsss_homework_2",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

