from test_aiti.infrastructure.persistence_sqla.mappings.category import (
    map_categories_table,
)
from test_aiti.infrastructure.persistence_sqla.mappings.client import map_clients_table
from test_aiti.infrastructure.persistence_sqla.mappings.nomenclature import (
    map_nomenclatures_table,
)
from test_aiti.infrastructure.persistence_sqla.mappings.order import map_orders_table
from test_aiti.infrastructure.persistence_sqla.mappings.order_item import (
    map_order_items_table,
)


def map_tables() -> None:
    map_clients_table()
    map_categories_table()
    map_nomenclatures_table()
    map_orders_table()
    map_order_items_table()
