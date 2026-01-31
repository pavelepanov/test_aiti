from sqlalchemy.ext.asyncio import AsyncSession

from test_aiti.application.interfaces.nomenclature_data_gateway import (
    NomenclatureDataGateway,
)
from test_aiti.models.nomenclature import Nomenclature, NomenclatureId


class NomenclatureDataMapperSqla(NomenclatureDataGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_by_id(self, id: NomenclatureId) -> Nomenclature | None:
        return await self._session.get(Nomenclature, id)
