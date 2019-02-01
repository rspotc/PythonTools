# This will try to import setuptools. If not here, it will reach for the embedded
# ez_setup (or the ez_setup package). If none, it fails with a message
try:
    from setuptools import setup
except ImportError:
    try:
        import ez_setup
        ez_setup.use_setuptools()
    except ImportError:
        raise ImportError("Python Tools could not be installed, probably because"
            " neither setuptools nor ez_setup are installed on this computer."
            "\nInstall ez_setup ([sudo] pip install ez_setup) and try again.")

from setuptools import setup, find_packages

exec(open('PythonTools/version.py').read()) # loads __version__

setup(name='PythonTools',
      version=__version__,
      author='Alec Hammond',
    description='Popular python tools',
    license='see LICENSE.txt',
    keywords="Python tools")
