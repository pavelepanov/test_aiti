from dataclasses import dataclass
from uuid import UUID

from test_aiti.application.errors import (
    MessagesError,
    NomenclatureDoesNotExistError,
    NotEnoughStockInStockError,
    OrderDoesNotExistError,
)
from test_aiti.application.interfaces.nomenclature_data_gateway import (
    NomenclatureDataGateway,
)
from test_aiti.application.interfaces.order_data_gateway import OrderDataGateway
from test_aiti.application.interfaces.order_item_data_gateway import (
    OrderItemDataGateway,
)
from test_aiti.application.interfaces.order_item_id_genrator import OrderItemIdGenerator
from test_aiti.application.interfaces.transaction_manager import TransactionManager
from test_aiti.models.nomenclature import (
    Nomenclature,
    NomenclatureId,
    NomenclatureQuantity,
)
from test_aiti.models.order import Order, OrderId
from test_aiti.models.order_item import (
    OrderItem,
    OrderItemId,
    OrderItemPriceAtPurchase,
    OrderItemQuantity,
    create_order_item,
)


@dataclass
class AddProductToOrderRequest:
    order_id: OrderId
    nomenclature_id: NomenclatureId
    quantity: OrderItemQuantity


class AddProductToOrderInteractor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        nomenclature_data_gateway: NomenclatureDataGateway,
        order_data_gateway: OrderDataGateway,
        order_item_data_gateway: OrderItemDataGateway,
        order_item_id_generator: OrderItemIdGenerator,
    ) -> None:
        self._transaction_manager = transaction_manager
        self._nomenclature_data_gateway = nomenclature_data_gateway
        self._order_data_gateway = order_data_gateway
        self._order_item_data_gateway = order_item_data_gateway
        self._order_item_id_generator = order_item_id_generator

    async def __call__(self, request: AddProductToOrderRequest) -> None:
        nomenclature: (
            Nomenclature | None
        ) = await self._nomenclature_data_gateway.read_by_id(request.nomenclature_id)
        if nomenclature is None:
            raise NomenclatureDoesNotExistError(
                MessagesError.NOMENCLATURE_DOES_NOT_EXIST
            )
        if nomenclature.quantity < request.quantity:
            raise NotEnoughStockInStockError(MessagesError.NOT_ENOUGH_STOCK_IN_STOCK)

        order: Order | None = await self._order_data_gateway.read_by_id(
            request.order_id
        )
        if order is None:
            raise OrderDoesNotExistError(MessagesError.ORDER_DOES_NOT_EXIST)

        existing_position: (
            OrderItem | None
        ) = await self._order_item_data_gateway.read_from_order(
            order.id, nomenclature.id
        )

        if existing_position:
            new_order_item_quantity = int(existing_position.quantity) + int(
                request.quantity
            )
            existing_position.quantity = OrderItemQuantity(new_order_item_quantity)
        else:
            order_item_id: OrderItemId = self._order_item_id_generator()
            order_item_quantity: OrderItemQuantity = OrderItemQuantity(request.quantity)
            order_item_price_at_purchase: OrderItemPriceAtPurchase = (
                OrderItemPriceAtPurchase(nomenclature.price)
            )
            order_item: OrderItem = create_order_item(
                id=order_item_id,
                quantity=order_item_quantity,
                price_at_purchase=order_item_price_at_purchase,
                order_id=order.id,
                nomenclature_id=nomenclature.id,
            )
            await self._order_item_data_gateway.add(order_item)

        new_nomenclature_quantity = int(nomenclature.quantity) - int(request.quantity)
        nomenclature.quantity = NomenclatureQuantity(new_nomenclature_quantity)

        await self._transaction_manager.commit()
