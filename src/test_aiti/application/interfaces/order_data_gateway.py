from abc import abstractmethod
from typing import Protocol

from test_aiti.models.order import Order, OrderId


class OrderDataGateway(Protocol):
    @abstractmethod
    async def read_by_id(id: OrderId) -> Order | None: ...
