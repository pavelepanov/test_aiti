from sqlalchemy import UUID, Column, ForeignKey, Integer, String, Table

from test_aiti.infrastructure.persistence_sqla.orm_registry import mapping_registry
from test_aiti.models.nomenclature import Nomenclature

nomenclatures_table = Table(
    "nomenclatures",
    mapping_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("title", String, nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("price", Integer, nullable=False),
    Column("category_id", UUID, ForeignKey("categories.id"), nullable=False),
)


def map_nomenclatures_table() -> None:
    mapping_registry.map_imperatively(
        Nomenclature,
        nomenclatures_table,
    )
