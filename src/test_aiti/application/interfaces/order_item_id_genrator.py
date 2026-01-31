from typing import Protocol

from test_aiti.models.order_item import OrderItemId


class OrderItemIdGenerator(Protocol):
    def __call__(self) -> OrderItemId: ...
