from setuptools import setup, find_packages


setup(
    dependency_links=[
        'http://github.com/victorlacorte/Nutri.git@dev#egg=nutri',
    ],
    entry_points={
        'console_scripts': [
            'unix-csv=nutri.scripts.gen_unix_csv:main',
        ],
    },
    name='nutri',
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    version='0.0',
    tests_require=[
        'pytest',
    ],
    # install_requires=[
    # ],
)
