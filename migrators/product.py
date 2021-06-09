from termcolor import cprint

from .abc import MigratorBase
from .adapters import ProductToProduct
from .category import CategoryMigrator
from .connection import get_prestashop


class ProductMigrator(MigratorBase):
    dependencies = [CategoryMigrator]

    def execute_migrate(self):
        prestashop_products = self.get_presta_products()
        total_count = len(prestashop_products)

        for index, presta_product in enumerate(prestashop_products):
            cprint(f"migrating {index+1} of {total_count}...", "yellow", end="\r")
            adapter = ProductToProduct(presta_product)
            shopify_product = adapter.to_shopify()
            self.__class__.id_counterparts[
                presta_product["product"]["id"]
            ] = shopify_product.id

        cprint(f"\n'{self.name}' migration finished!", "green")

    def get_presta_products(self):
        prestashop = get_prestashop()
        product_ids = prestashop.search("products")
        products = []

        for product_id in product_ids:
            product = prestashop.get("products", resource_id=product_id)
            products.append(product)

        return products
