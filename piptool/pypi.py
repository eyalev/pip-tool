from piptool.pypi_project import PyPiProject


class PyPi:

    @classmethod
    def get_project(cls, project_name):
        project = PyPiProject.get_project(project_name)
        return project
