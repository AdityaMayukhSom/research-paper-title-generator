import fastapi
import fastapi.staticfiles
import fastapi.middleware.cors

from .routes import api_router


class SummarizationApplication:
    __allowed_origins = [
        "http://localhost:5173",
    ]
    __allowed_headers: list[str] = ["*"]
    __allowed_methods: list[str] = ["*"]
    __allowed_credentials: bool = True
