'''Setup script for download_water_data.'''

from distutils import cmd
import zipapp
import os.path
from setuptools import setup
from download_water_data.__main__ import __version__

SRC_DIR = os.path.abspath(os.path.dirname(__file__))

class PyzCommand(cmd.Command):
    '''A custom command to generate download_water_data.pyz.'''

    description = 'generate download_water_data.pyz'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        '''Run command.'''
        out_dir = os.path.join(SRC_DIR, 'dist')
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        with open(os.path.join(SRC_DIR, 'download_water_data', '__main__.py'), 'rb') as main:
            zipapp.create_archive(main, os.path.join(out_dir, 'download_water_data.pyz'))

setup(
    cmdclass={
        'pyz': PyzCommand,
    },
    name='download_water_data',
    version=__version__,
    description='Downloader for the Global Surface Water Data of the Copernicus Programme',
    long_description=open(os.path.join(SRC_DIR, 'README.rst'), 'r').read(),
    url='https://github.com/mentaljam/download_water_data',
    author='Petr Tsymbarovich',
    author_email='petr@tsymbarovich.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    keywords='Copernicus global surface water download',
    packages=['download_water_data'],
    entry_points={
        'console_scripts': ['download_water_data=download_water_data.__main__:main']
    }
)
