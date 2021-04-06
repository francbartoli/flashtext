from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)

name = 'pyflashtext'
version = '2.7'

cmdclass = {'test': PyTest}

try:
    from sphinx.setup_command import BuildDoc
    cmdclass['build_sphinx'] = BuildDoc
except ImportError:
    print('WARNING: sphinx not available, not building docs')

setup(
    name=name,
    version=version,
    url='http://github.com/francbartoli/pyflashtext',
    author='Francesco Bartoli',
    author_email='xbartolone@gmail.com',
    description='Extract/Replaces keywords in sentences.',
    long_description=open('README.rst').read(),
    packages=['pyflashtext'],
    install_requires=[],
    platforms='any',
    cmdclass=cmdclass,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', version)
        }
    }
)
