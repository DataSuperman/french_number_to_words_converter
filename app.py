from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from logic.number_to_words_converter import FrenchNumberToWordsConverter

app = FastAPI()


class NumberList(BaseModel):
    numbers: List[int]


@app.post("/convert/")
async def convert(number_list: NumberList):
    converter = FrenchNumberToWordsConverter()
    french_numbers = [converter.convert(number) for number in number_list.numbers]
    return {"numbers": number_list.numbers, "french_numbers": french_numbers}
