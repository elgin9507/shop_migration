from migrators import CategoryMigrator, ProductMigrator


def migrate():
    migrations = [CategoryMigrator("categories"), ProductMigrator("products")]

    for migration in migrations:
        migration.migrate()


if __name__ == "__main__":
    migrate()
