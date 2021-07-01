from setuptools import find_packages, setup
setup(
    name='cowinPY',
    packages=find_packages(include=['cowinPy']),
    version='0.1.0',
    description='A python wrapper for cowin public ais.',
    author='techhub',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    
)