#!/usr/bin/env python

from setuptools import setup, find_packages


def read_requirements(filename):
    with open(filename) as f:
        requirements = [
            line[:line.find('#')] for line in f.read().splitlines()
            if not line.startswith('-i') and not line.startswith('#')
        ]


with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = read_requirements('requirements.txt')
test_requirements = read_requirements('dev-requirements.txt')

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Intended Audience :: Developers',

        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:cli',
        ],
    },
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)

