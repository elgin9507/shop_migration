# Python app for migrating data from prestashop to shopify (only products and categories)

## Steps for running in local:
  - You must provide `.env` file at root folder that contains credentials for shopify and prestashop. Sample `.env` file content:

        SHOPIFY_SHOP_URL=https://my_shop_name.myshopify.com/
        SHOPIFY_API_VERSION=2021-04
        SHOPIFY_TOKEN=secret_token
        PRESTASHOP_WEBSERVICE_URL=http://prestashop.domain/api
        PRESTASHOP_WEBSERVICE_KEY=secret_webservice_key
      
  - Run: `python migrate.py`

#### Note: This is just a test task, not intended for real usage
