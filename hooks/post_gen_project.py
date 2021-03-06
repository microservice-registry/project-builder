#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if '{{ cookiecutter.dockerized }}' != 'y':
        remove_file('Dockerfile')

    if '{{ cookiecutter.python }}' != 'y':
        shutil.rmtree('{{ cookiecutter.project_slug }}')
        remove_file('setup.py')
        remove_file('requirements_dev.txt')
        remove_file('MANIFEST.in')
        remove_file('setup.cfg')
        remove_file('travis_pypi_setup.py')
        shutil.rmtree('tests')
        remove_file('Makefile')
        remove_file('CONTRIBUTING.rst')

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if 'Click' != '{{ cookiecutter.command_line_interface }}':
        shutil.rmtree(os.path.join('{{ cookiecutter.project_slug }}',
            'commands'))
