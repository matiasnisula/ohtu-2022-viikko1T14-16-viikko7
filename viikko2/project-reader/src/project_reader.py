from ast import parse
from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        name =""
        description =""
        dependencies = []
        dev_dependencies = []

        parsed_toml = toml.loads(content)

        for key_1 in parsed_toml:
            if key_1 == "tool":
                tool = parsed_toml["tool"]
                for key_2 in tool:
                    if key_2 == "poetry":
                        poetry = tool[key_2]
                        for key_3 in poetry:

                            if key_3 == "name":
                                name = poetry[key_3]
                                
                            elif key_3 == "description":
                                description = poetry[key_3]

                            elif key_3 == "dependencies":
                                for dependencie in poetry[key_3]:
                                    dependencies.append(dependencie)
                                
                            elif key_3 == "dev-dependencies":
                                for dev_dep in poetry[key_3]:
                                    dev_dependencies.append(dev_dep)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
