from typing import AsyncIterable

from dishka import (
    AsyncContainer,
    Provider,
    Scope,
    from_context,
    make_async_container,
    provide,
)
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from test_aiti.application.interactors.add_product_to_order import (
    AddProductToOrderInteractor,
)
from test_aiti.application.interfaces.nomenclature_data_gateway import (
    NomenclatureDataGateway,
)
from test_aiti.application.interfaces.order_data_gateway import OrderDataGateway
from test_aiti.application.interfaces.order_item_data_gateway import (
    OrderItemDataGateway,
)
from test_aiti.application.interfaces.order_item_id_genrator import (
    OrderItemIdGenerator,
)
from test_aiti.application.interfaces.transaction_manager import TransactionManager
from test_aiti.entrypoint.config import Config
from test_aiti.infrastructure.adapters.nomenclature_data_mapper_sqla import (
    NomenclatureDataMapperSqla,
)
from test_aiti.infrastructure.adapters.order_data_mapper_sqla import (
    OrderDataMapperSqla,
)
from test_aiti.infrastructure.adapters.order_item_data_mapper_sqla import (
    OrderItemDataMapperSqla,
)
from test_aiti.infrastructure.adapters.order_item_id_generator_uuid import (
    OrderItemIdGeneratorUUID,
)
from test_aiti.infrastructure.adapters.transaction_manager_sqla import (
    TransactionManagerSqla,
)


class ConfigProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)


class PostgresProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_engine(self, config: Config) -> AsyncEngine:
        return create_async_engine(config.postgres_config.uri)

    @provide(scope=Scope.APP)
    def provide_sessionmaker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def provide_transaction_manager(self, session: AsyncSession) -> TransactionManager:
        return TransactionManagerSqla(session)

    @provide(scope=Scope.REQUEST)
    def provide_nomenclature_data_gateway(
        self,
        session: AsyncSession,
    ) -> NomenclatureDataGateway:
        return NomenclatureDataMapperSqla(session)

    @provide(scope=Scope.REQUEST)
    def provide_order_data_gateway(
        self,
        session: AsyncSession,
    ) -> OrderDataGateway:
        return OrderDataMapperSqla(session)

    @provide(scope=Scope.REQUEST)
    def provide_order_item_data_gateway(
        self,
        session: AsyncSession,
    ) -> OrderItemDataGateway:
        return OrderItemDataMapperSqla(session)


class IdGeneratorsProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_order_item_id_generator(self) -> OrderItemIdGenerator:
        return OrderItemIdGeneratorUUID()


class InteractorsProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def provide_add_product_to_order_interactor(
        self,
        transaction_manager: TransactionManager,
        nomenclature_data_gateway: NomenclatureDataGateway,
        order_data_gateway: OrderDataGateway,
        order_item_data_gateway: OrderItemDataGateway,
        order_item_id_generator: OrderItemIdGenerator,
    ) -> AddProductToOrderInteractor:
        return AddProductToOrderInteractor(
            transaction_manager,
            nomenclature_data_gateway,
            order_data_gateway,
            order_item_data_gateway,
            order_item_id_generator,
        )


def create_async_ioc_container(config: Config) -> AsyncContainer:
    return make_async_container(
        PostgresProvider(),
        IdGeneratorsProvider(),
        InteractorsProvider(),
        context={Config: config},
    )
