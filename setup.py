from setuptools import setup, find_packages

requires = [
    "zope.interface",
]

tests_require = [
    "pytest",
]

setup(
    name='rebecca.workflow',
    version='0.0',
    packages=find_packages(),
    package_dir={"": "src"},
    url='https://github.com/rebeccaframework/rebecca.workflow',
    license='MIT',
    author='Atsushi Odagiri',
    author_email='aodagx@gmail.com',
    description='workflow',
    install_requires=requires,
    tests_require=tests_require,
)
