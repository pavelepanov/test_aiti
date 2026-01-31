from sqlalchemy import UUID, BigInteger, Column, String, Table, Text
from sqlalchemy.orm import relationship

from test_aiti.infrastructure.persistence_sqla.orm_registry import mapping_registry
from test_aiti.models.client import Client

clients_table = Table(
    "clients",
    mapping_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("title", String, nullable=False),
    Column("address", String, nullable=True),
)


def map_clients_table() -> None:
    mapping_registry.map_imperatively(
        Client,
        clients_table,
    )
