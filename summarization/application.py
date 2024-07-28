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

    @classmethod
    def generate(cls):
        app = fastapi.FastAPI()

        app.add_middleware(
            fastapi.middleware.cors.CORSMiddleware,
            allow_origins=cls.__allowed_origins,
            allow_methods=cls.__allowed_methods,
            allow_headers=cls.__allowed_headers,
            allow_credentials=cls.__allowed_credentials,
        )

        app.include_router(api_router)

        return app
