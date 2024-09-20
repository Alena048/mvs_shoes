import re

from pydantic import BaseModel, field_validator


class Shoes(BaseModel):
    id: str
    type: str
    model: str
    color: str
    price: str
    manufacturer: str
    size: str

    @field_validator("model", "color", "manufacturer")
    @classmethod
    def validate_type(cls, values: str) -> str:
        if not re.match(r'^[А-Я][а-яё]*$', values):
            raise ValueError('Должно быть написано с большой буквы')
        return values

    @field_validator("type")
    @classmethod
    def validate_pol(cls, values: str) -> str:
        if not re.fullmatch(r'(МУЖ)|(ЖЕН)', values):
            raise ValueError('Должно быть указано только МУЖ или ЖЕН')
        return values

