from fastapi import APIRouter
from pydantic import BaseModel, Field

import horoscoper.nlp
from horoscoper import utils


__all__ = ["api_router"]

api_router = APIRouter(prefix="/v1")


class PredictionPost(BaseModel):
    day: str = Field()
    category: str = Field()
    sign: str = Field()


@api_router.post("/predict")
def get_horoscope_prediction(features: PredictionPost):
    prompt = utils.make_prompt(features.dict())

    pred = horoscoper.nlp.get_prediction_from_prompt(prompt)

    horoscope = utils.extract_horoscope(pred)
    return {
        "data": pred,
        "horoscope": horoscope,
    }
