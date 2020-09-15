import urllib.parse

from django.urls import reverse


def test_api_parse_success(client, success_response):
    address_string = "123 main st chicago il"
    url = (reverse("address-parse") + "?address="
           + urllib.parse.quote(address_string))
    response = client.get(url)

    assert response.status_code == 200
    assert response.json() == success_response


def test_api_parse_raise_error(client, error_response):
    address_string = "123 main st chicago il 123 main st"
    url = (reverse("address-parse") + "?address="
           + urllib.parse.quote(address_string))
    response = client.get(url)

    assert response.status_code == 400
    assert response.json() == error_response
