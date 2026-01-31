from enum import StrEnum


class MessagesError(StrEnum):
    NOMENCLATURE_DOES_NOT_EXIST = "Nomenclature does not exist."
    NOT_ENOUGH_STOCK_IN_STOCK = "Not enough stock in stock."
    ORDER_DOES_NOT_EXIST = "Order does not exist."


class NomenclatureDoesNotExistError(Exception): ...


class NotEnoughStockInStockError(Exception): ...


class OrderDoesNotExistError(Exception): ...
