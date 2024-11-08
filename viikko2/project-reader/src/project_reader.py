from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        thisistoml=toml.loads(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        print(thisistoml)
        return Project(thisistoml["tool"]["poetry"]["name"], thisistoml["tool"]["poetry"]["description"], thisistoml["tool"]["poetry"]["license"], thisistoml["tool"]["poetry"]["authors"], thisistoml["tool"]["poetry"]["dependencies"], thisistoml["tool"]["poetry"]["group"]["dev"]["dependencies"])
#new=ProjectReader("https://raw.githubusercontent.com/ohjelmistotuotanto-hy/tehtavat/main/viikko2/test-project/pyproject.toml")
#print(new.get_project())