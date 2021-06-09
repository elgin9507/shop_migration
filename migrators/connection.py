import shopify
from prestapyt import PrestaShopWebServiceDict

from . import config

_shopify = None
_prestashop = None


def get_shopify():
    global _shopify
    if _shopify is not None:
        return _shopify

    session = shopify.Session(
        shop_url=config.SHOPIFY_SHOP_URL,
        version=config.SHOPIFY_API_VERSION,
        token=config.SHOPIFY_TOKEN,
    )
    shopify.ShopifyResource.activate_session(session)
    _shopify = shopify

    return _shopify


def get_prestashop():
    global _prestashop
    if _prestashop is not None:
        return _prestashop

    prestashop = PrestaShopWebServiceDict(
        config.PRESTASHOP_WEBSERVICE_URL, config.PRESTASHOP_WEBSERVICE_KEY
    )
    _prestashop = prestashop

    return prestashop
