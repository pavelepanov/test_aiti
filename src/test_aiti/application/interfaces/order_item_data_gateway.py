from abc import abstractmethod
from typing import Protocol

from test_aiti.models.nomenclature import NomenclatureId
from test_aiti.models.order import OrderId
from test_aiti.models.order_item import OrderItem


class OrderItemDataGateway(Protocol):
    @abstractmethod
    async def read_from_order(
        order_id: OrderId, nomenclature_id: NomenclatureId
    ) -> OrderItem | None: ...

    @abstractmethod
    async def add(order_item: OrderItem) -> None: ...
