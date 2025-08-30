from setuptools import setup, find_packages

setup(
    name='client',
    version='0.1.0',
    description='A python client for Idle Heroes',
    author='yntha',
    author_email='126660548+yntha@users.noreply.github.com',
    url='https://github.com/yntha/client',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'protobuf',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': ['ih-client=client.app:cli_entry',],
    },
)