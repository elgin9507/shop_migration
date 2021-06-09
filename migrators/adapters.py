import shopify

from .abc import AdapterBase
from .connection import get_prestashop, get_shopify


class CategoryToCollection(AdapterBase):
    def to_shopify(self):
        shopify = get_shopify()
        attrs = {
            "title": self.presta_item["name"]["language"]["value"],
            "body_html": self.presta_item["description"]["language"]["value"],
        }
        collection = shopify.CustomCollection(attributes=attrs)
        collection.save()

        return collection


class ProductToProduct(AdapterBase):
    def to_shopify(self):
        shopify = get_shopify()
        prestashop = get_prestashop()

        prestashop_supplier = prestashop.get(
            "suppliers", resource_id=self.presta_item["product"]["id_supplier"]
        )["supplier"]
        prestashop_category = prestashop.get(
            "categories", resource_id=self.presta_item["product"]["id_category_default"]
        )["category"]
        # TODO prestashop combinations must be converted to shopify variants
        prestashop_comb_ids = [
            c["id"]
            for c in self.presta_item["product"]["associations"]["combinations"][
                "combination"
            ]
        ]

        attrs = {
            "title": self.presta_item["product"]["name"]["language"]["value"],
            "body_html": self.presta_item["product"]["description"]["language"][
                "value"
            ],
            "vendor": prestashop_supplier["name"],
            "product_type": prestashop_category["name"]["language"]["value"],
            "status": "active"
            if self.presta_item["product"]["active"] == "1"
            else "draft",
        }

        product = shopify.Product(attributes=attrs)
        product.save()
        self.migrate_categories(product)

        return product

    def migrate_categories(self, product):
        from .category import CategoryMigrator

        prestashop_category_ids = [
            c["id"]
            for c in self.presta_item["product"]["associations"]["categories"][
                "category"
            ]
        ]

        for presta_category_id in prestashop_category_ids:
            shopify_collection_id = CategoryMigrator.id_counterparts[presta_category_id]
            collect = shopify.Collect(
                {"product_id": product.id, "collection_id": shopify_collection_id}
            )
            collect.save()
