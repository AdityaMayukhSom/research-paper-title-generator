import fastapi
import fastapi.responses
import pydantic
import transformers
import huggingface_hub
import os


api_router = fastapi.APIRouter(prefix="/api")
