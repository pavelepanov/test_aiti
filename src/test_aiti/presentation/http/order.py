from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException, status

from test_aiti.application.errors import (
    NomenclatureDoesNotExistError,
    NotEnoughStockInStockError,
    OrderDoesNotExistError,
)
from test_aiti.application.interactors.add_product_to_order import (
    AddProductToOrderInteractor,
    AddProductToOrderRequest,
)

order_router = APIRouter()


@order_router.post("/order", status_code=status.HTTP_201_CREATED)
@inject
async def add_product_to_order(
    request: AddProductToOrderRequest,
    interactor: FromDishka[AddProductToOrderInteractor],
) -> None:
    try:
        await interactor(request)
    except (NomenclatureDoesNotExistError, OrderDoesNotExistError) as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except NotEnoughStockInStockError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
