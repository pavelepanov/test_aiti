from sqlalchemy.ext.asyncio import AsyncSession

from test_aiti.application.interfaces.transaction_manager import TransactionManager


class TransactionManagerSqla(TransactionManager):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self):
        await self._session.commit()
