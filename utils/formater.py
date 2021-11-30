import re


def clean_html(text: str):
    return re.sub('<.*?>', '', text)
