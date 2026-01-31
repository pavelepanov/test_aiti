from dataclasses import dataclass
from typing import NewType
from uuid import UUID

ClientId = NewType("ClientId", UUID)
ClientTitle = NewType("ClientTitle", str)
ClientAddress = NewType("ClientAddress", str)


@dataclass
class Client:
    id: ClientId
    title: ClientTitle
    address: ClientAddress


def create_client(
    id: ClientId,
    title: ClientTitle,
    address: ClientAddress,
) -> Client:
    return Client(
        id=id,
        title=title,
        address=address,
    )
