import io, os, re
from setuptools import setup, find_packages

def read(*names, **kwargs):
    with io.open(
            os.path.join(os.path.dirname(__file__), *names),
            encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(name='zebra-zpl',
      version=find_version('zebra_zpl', '__init__.py'),
      description='Python library to generate usable and printable ZPL2 code',
      url='https://github.com/mtking2/py-zebra-zpl',
      author='Michael King',
      author_email='mking@hey.com',
      license='MIT',
      keywords='zebra zpl zpl2 label printer',
      packages=find_packages(exclude=[]),
      install_requires=[],
      zip_safe=False)
