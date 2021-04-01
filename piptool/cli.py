
import click
from piptool.pypi import PyPi


@click.group()
def cli():
    pass


@cli.command()
@click.argument('project_name')
def requirement(project_name):
    project = PyPi.get_project(project_name)
    print(f'{project_name}=={project.latest_version_id}')


@cli.command()
@click.argument('project_name')
def requirement_pyproject(project_name):
    project = PyPi.get_project(project_name)
    print(f'{project_name} = "{project.latest_version_id}"')

