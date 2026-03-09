import re

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"


def extract_entities(text: str):
    return {"emails": re.findall(EMAIL_REGEX, text)}
