from setuptools import setup, find_packages

setup(
    name='gym_notices',
    version='0.0',
    license='MIT',
    author="Farama Foundation",
    author_email='contact@farama.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Farama-Foundation/gym-notices',
    keywords='gym, notices',
)
