import pytest


@pytest.fixture
def success_response():
    return {
        "input_string": "123 main st chicago il",
        "address_components": {
            "AddressNumber": "123",
            "StreetName": "main",
            "StreetNamePostType": "st",
            "PlaceName": "chicago",
            "StateName": "il",
        },
        "address_type": "Street Address",
    }


@pytest.fixture
def error_response():
    return {"error": "Unable to parse this value due to repeated labels."}
