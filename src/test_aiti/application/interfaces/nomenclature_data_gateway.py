from abc import abstractmethod
from typing import Protocol

from test_aiti.models.nomenclature import Nomenclature, NomenclatureId


class NomenclatureDataGateway(Protocol):
    @abstractmethod
    async def read_by_id(self, id: NomenclatureId) -> Nomenclature | None: ...
