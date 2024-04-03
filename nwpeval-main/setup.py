from setuptools import setup, find_packages

setup(
    name='nwpeval',
    version='1.5.0b2',
    description='A package for computing metrics for NWP model evaluation',
    author='Debasish Mahapatra',
    author_email='debasish.atmos@gmail.com | debasish.mahapatra@ugent.be',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pygrib',
        'xarray',
        'scipy',
        'pandas',
        'matplotlib',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
)