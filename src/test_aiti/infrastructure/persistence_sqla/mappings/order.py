from sqlalchemy import UUID, Column, DateTime, ForeignKey, Table

from test_aiti.infrastructure.persistence_sqla.orm_registry import mapping_registry
from test_aiti.models.order import Order

orders_table = Table(
    "orders",
    mapping_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("created_at", DateTime, nullable=False),
    Column("client_id", UUID, ForeignKey("clients.id"), nullable=False),
)


def map_orders_table() -> None:
    mapping_registry.map_imperatively(
        Order,
        orders_table,
    )
