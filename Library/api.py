from ninja_extra import NinjaExtraAPI
from Books import controllers


api = NinjaExtraAPI(
    title="Library API",
    version="1.0.0",
    urls_namespace="library_api"
)

api.register_controllers(controllers.BookController)