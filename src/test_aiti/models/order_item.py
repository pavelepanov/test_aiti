from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from test_aiti.models.nomenclature import NomenclatureId
from test_aiti.models.order import OrderId

OrderItemId = NewType("OrderItemId", UUID)
OrderItemQuantity = NewType("OrderItemQuantity", int)
OrderItemPriceAtPurchase = NewType("OrderItemPriceAtPurchase", int)


@dataclass
class OrderItem:
    id: OrderItemId
    quantity: OrderItemQuantity
    price_at_purchase: OrderItemPriceAtPurchase
    order_id: OrderId
    nomenclature_id: NomenclatureId


def create_order_item(
    id: OrderItemId,
    quantity: OrderItemQuantity,
    price_at_purchase: OrderItemPriceAtPurchase,
    order_id: OrderId,
    nomenclature_id: NomenclatureId,
) -> OrderItem:
    return OrderItem(
        id=id,
        quantity=quantity,
        price_at_purchase=price_at_purchase,
        order_id=order_id,
        nomenclature_id=nomenclature_id,
    )
