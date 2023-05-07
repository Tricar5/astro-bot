__all__ = ["make_prompt", "extract_horoscope"]


def make_prompt(data) -> str:
    return f"день {data['day']} категория {data['category']} для знака {data['sign']} Гороскоп:"


def extract_horoscope(s: str) -> str:
    return s.split("ороскоп:", 1)[1].strip()
