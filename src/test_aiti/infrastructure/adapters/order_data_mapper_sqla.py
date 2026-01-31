from sqlalchemy.ext.asyncio import AsyncSession

from test_aiti.application.interfaces.order_data_gateway import OrderDataGateway
from test_aiti.models.order import Order, OrderId


class OrderDataMapperSqla(OrderDataGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_by_id(self, id: OrderId) -> Order | None:
        return await self._session.get(Order, id)
