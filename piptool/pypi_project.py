from typing import Type, Union

import requests


class PyPiProject:

    def __init__(self, project_name):
        self._project_name = project_name
        self._data = None

    @property
    def project_name(self):
        return self._project_name

    @property
    def data(self) -> dict:

        if self._data is not None:
            return self._data

        url = f"https://pypi.org/pypi/{self.project_name}/json"

        response = requests.get(url)
        data = response.json()

        self._data = data
        return self._data

    @property
    def info(self) -> dict:
        return self.data['info']

    @property
    def latest_version_id(self):
        return self.info['version']

    @property
    def releases(self) -> dict:
        return self.data['releases']

    @property
    def latest_version_packages(self) -> list:
        return self.releases[self.latest_version_id]

    @property
    def latest_version_dist(self):
        result_list = [package for package in self.latest_version_packages if package['packagetype'] == 'sdist']
        assert len(result_list) == 1
        dist_data = result_list[0]
        return dist_data

    @classmethod
    def get_project(cls, project_name):
        """
        :rtype: PyPiProject
        """
        project = PyPiProject(project_name)
        return project
