from fastapi import FastAPI

from src.controller.test_controller import test_router
from src.controller.item_controller  import item_router
from src.controller.data_source_controller import data_source_router
from src.controller.item_price_controller import item_price_router
from src.controller.crafting_slot_controller import crafting_slot_router


def setup_routes(app: FastAPI, prefix: str):
   app.include_router(test_router, prefix=prefix)
   app.include_router(item_router, prefix=prefix)
   app.include_router(data_source_router, prefix=prefix)
   app.include_router(item_price_router, prefix=prefix)
   app.include_router(crafting_slot_router, prefix=prefix)