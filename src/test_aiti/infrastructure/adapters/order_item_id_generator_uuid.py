import uuid

from test_aiti.application.interfaces.order_item_id_genrator import (
    OrderItemIdGenerator,
)
from test_aiti.models.order_item import OrderItemId


class OrderItemIdGeneratorUUID(OrderItemIdGenerator):
    def __call__(self) -> OrderItemId:
        return OrderItemId(uuid.uuid4())
