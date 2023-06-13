"""
django-gm2m
Django generic many-to-many field
(c) 2014-2020 Thomas Khyn
MIT License (see LICENSE.txt)
"""

from setuptools import setup, find_packages
import os


# imports __version__ variable
exec(open('gm2m/version.py').read())

# setup function parameters
setup(
    name='django-gm2m',
    version=__version__,
    description='Django generic many-to-many field',
    long_description=open(os.path.join('README.rst')).read(),
    author='Thomas Khyn',
    author_email='thomas@ksytek.com',
    url='https://github.com/tkhyn/django-gm2m',
    keywords=['django', 'generic', 'many-to-many'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Environment :: Other Environment',
    ],
    packages=find_packages(exclude=('tests',)),
    install_requires=(
        'Django>=2.2',
    ),
    zip_safe=True,
)
