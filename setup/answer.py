import requests
from constants import *
from scrape import get_headers


def submit_answer(day: int, answer: str):
    headers = get_headers()
    data = {
        "level": "1",
        "answer": answer,
    }

    response = requests.post(
        ARTICLE_ENDPOINT.replace("XX", str(day)),
        headers=headers,
        data=data,
    )
