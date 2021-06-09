from abc import ABC, abstractmethod

from termcolor import cprint


class MigratorBase(ABC):
    dependencies = []
    _applied = False
    id_counterparts = {}

    def __init__(self, name):
        self.name = name

    def migrate(self):
        self.check_dependencies()
        cprint(f"starting '{self.name}' migration...", "yellow")
        self.execute_migrate()
        self.__class__._applied = True

    @abstractmethod
    def execute_migrate(self):
        ...

    def check_dependencies(self):
        for dependency in self.dependencies:
            if not dependency._applied:
                raise RuntimeError(
                    f"{dependency} sould be applied firstly before executing {self.name}"
                )


class AdapterBase(ABC):
    def __init__(self, presta_item):
        self.presta_item = presta_item

    @abstractmethod
    def to_shopify(self):
        ...
