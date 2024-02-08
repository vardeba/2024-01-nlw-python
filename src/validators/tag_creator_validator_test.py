from src.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)
from .tag_creator_validator import tag_create_validator


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_create_validator():
    req = MockRequest(json={"product_code": "12345"})
    tag_create_validator(req)


def test_tag_create_validator_with_error():
    req = MockRequest(json={"product_code": 12345})

    try:
        tag_create_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
