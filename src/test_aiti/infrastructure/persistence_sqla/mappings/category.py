from sqlalchemy import UUID, Column, ForeignKey, String, Table

from test_aiti.infrastructure.persistence_sqla.orm_registry import mapping_registry
from test_aiti.models.category import Category

categories_table = Table(
    "categories",
    mapping_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("title", String, nullable=False),
    Column(
        "parent_id",
        UUID,
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=True,
    ),
)


def map_categories_table() -> None:
    mapping_registry.map_imperatively(
        Category,
        categories_table,
    )
