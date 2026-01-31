from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from test_aiti.models.category import CategoryId

NomenclatureId = NewType("NomenclatureId", UUID)
NomenclatureTitle = NewType("NomenclatureTitle", str)
NomenclatureQuantity = NewType("NomenclatureQuantity", int)
NomenclaturePrice = NewType("NomenclaturePrice", int)


@dataclass
class Nomenclature:
    id: NomenclatureId
    title: NomenclatureTitle
    quantity: NomenclatureQuantity
    price: NomenclaturePrice
    category_id: CategoryId


def create_nomenclature(
    id: NomenclatureId,
    title: NomenclatureTitle,
    quantity: NomenclatureQuantity,
    price: NomenclaturePrice,
    category_id: CategoryId,
) -> Nomenclature:
    return Nomenclature(
        id=id,
        title=title,
        quantity=quantity,
        price=price,
        category_id=category_id,
    )
