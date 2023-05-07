from transformers import GPT2LMHeadModel, GPT2Tokenizer


__all__ = ["get_prediction_from_prompt"]

from horoscoper import settings


tok = GPT2Tokenizer.from_pretrained(settings.MODEL_PATH)

model = GPT2LMHeadModel.from_pretrained(settings.MODEL_PATH)
model.cpu()


def get_prediction_from_prompt(prompt: str):
    inpt = tok.encode(prompt, return_tensors="pt")
    out = model.generate(
        inpt.cpu(),
        max_length=settings.SEQUENCE_LENGTH,
        repetition_penalty=5.0,
        do_sample=True,
        top_k=5,
        top_p=0.95,
        temperature=settings.MODEL_TEMPERATURE,
    )

    return tok.decode(out[0]).split("\n")[0]
