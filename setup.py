from setuptools import setup
from setuptools.command.sdist import sdist 

setup(
    name='verbose_chainsaw',
    version='0.1.0',
    packages=['verbose_chainsaw'],
    url='https://github.com/egoughnour/verbose-chainsaw',
    license='MIT',
    author='E Goughnour',
    author_email='e.goughnour@gmail.com',
    description='A stub for testing barebones package generation for development',
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    cmdclass={
        'sdist': sdist
    }
)