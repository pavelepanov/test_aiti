from dataclasses import dataclass
from typing import NewType
from uuid import UUID

CategoryId = NewType("CategoryId", UUID)
CategoryTitle = NewType("CategoryTitle", str)


@dataclass
class Category:
    id: CategoryId
    title: CategoryTitle
    parent_id: CategoryId | None


def create_category(
    id: CategoryId,
    title: CategoryTitle,
    parent_id: CategoryId | None,
) -> Category:
    return Category(
        id=id,
        title=title,
        parent_id=parent_id,
    )
