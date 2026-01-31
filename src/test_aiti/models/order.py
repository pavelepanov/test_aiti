from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from test_aiti.models.client import ClientId

OrderId = NewType("OrderId", UUID)


@dataclass
class Order:
    id: OrderId
    created_at: datetime
    client_id: ClientId


def create_order(
    id: OrderId,
    created_at: datetime,
    client_id: ClientId,
) -> Order:
    return Order(
        id=id,
        created_at=created_at,
        client_id=client_id,
    )
