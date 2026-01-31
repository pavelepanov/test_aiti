from sqlalchemy import UUID, Column, ForeignKey, Integer, Table

from test_aiti.infrastructure.persistence_sqla.orm_registry import mapping_registry
from test_aiti.models.order_item import OrderItem

order_items_table = Table(
    "order_items",
    mapping_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("quantity", Integer, nullable=False),
    Column("price_at_purchase", Integer, nullable=False),
    Column("order_id", UUID, ForeignKey("orders.id"), nullable=False),
    Column(
        "nomenclature_id",
        UUID,
        ForeignKey("nomenclatures.id", ondelete="CASCADE"),
        nullable=False,
    ),
)


def map_order_items_table() -> None:
    mapping_registry.map_imperatively(
        OrderItem,
        order_items_table,
    )
