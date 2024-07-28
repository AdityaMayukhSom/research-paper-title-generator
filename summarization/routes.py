import fastapi
import fastapi.responses
import pydantic
import transformers
import huggingface_hub
import os


api_router = fastapi.APIRouter(prefix="/api")


@api_router.get("/available-models")
def available_models():
    available_models_list: list[str] = [
        "TohidaRehman/pegasus-large-Abstract-Title-CSPubSum",
        "TohidaRehman/t5-base-Abstract-Title",
        "TohidaRehman/bart-base-Abstract-Title-CSPubSum",
        "czearing/article-title-generator",
        "AryanLala/autonlp-Scientific_Title_Generator-34558227",
        "Fabby/gpt2-english-light-novel-titles",
    ]

    return {"models": available_models_list}


class SummarizationRequest(pydantic.BaseModel):
    elaborate_text: str
    summarization_model: str
    maximum_tokens: int
    use_huggingface_model: bool

