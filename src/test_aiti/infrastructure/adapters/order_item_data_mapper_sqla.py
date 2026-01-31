from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from test_aiti.application.interfaces.order_item_data_gateway import (
    OrderItemDataGateway,
)
from test_aiti.models.nomenclature import NomenclatureId
from test_aiti.models.order import OrderId
from test_aiti.models.order_item import OrderItem


class OrderItemDataMapperSqla(OrderItemDataGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_from_order(
        self, order_id: OrderId, nomenclature_id: NomenclatureId
    ) -> OrderItem | None:
        stmt = select(OrderItem).where(
            OrderItem.order_id == order_id,
            OrderItem.nomenclature_id == nomenclature_id,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def add(self, order_item: OrderItem) -> None:
        self._session.add(order_item)
