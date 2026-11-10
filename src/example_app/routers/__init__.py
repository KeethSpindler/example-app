from example_app.routers.core.core_router import get_core_router

def get_routes():
    return [
        get_core_router(),
    ]