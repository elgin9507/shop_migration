from termcolor import cprint

from .abc import MigratorBase
from .adapters import CategoryToCollection
from .connection import get_prestashop


class CategoryMigrator(MigratorBase):
    def execute_migrate(self):
        presta_categories = self.get_presta_categories()
        total_count = len(presta_categories)

        for index, category in enumerate(presta_categories):
            cprint(f"migrating {index+1} of {total_count}...", "yellow", end="\r")
            adapter = CategoryToCollection(category)
            collection = adapter.to_shopify()
            self.__class__.id_counterparts[category["id"]] = collection.id

        cprint(f"\n'{self.name}' migration finished!", "green")

    def get_presta_categories(self):
        prestashop = get_prestashop()
        categories = []
        category_ids = prestashop.search("categories")

        for category_id in category_ids:
            category = prestashop.get("categories", resource_id=category_id)
            categories.append(category["category"])

        return categories
