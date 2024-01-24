import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    # print(f"Response is {r.text}")
    # print(f"Response Body is {r.json()}")
    # print(f"Response Status code is {r.status_code}")
    # print(f"Response Headers are {r.headers}")

    url = r.json()
    headers = r.headers

    assert url['organizations_url'] == 'https://api.github.com/users/defunkt/orgs'
    assert r.status_code == 200
    assert headers['Content-Security-Policy'] == "default-src 'none'"


@pytest.mark.api_petstore
def test_swagger():
    base_url = 'https://petstore.swagger.io/v2/swagger.json'
    r = requests.get(base_url)

    add_pet = {
        "id": 1,
        "category": {
            "id": 1,
            "name": "Pes"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    r_post = requests.post('https://petstore.swagger.io/v2/pet', json=add_pet)
    r_get = requests.get('https://petstore.swagger.io/v2/pet/1')
    r_get_json = r_get.json()
    print(r_get_json)

    assert r.status_code == 200
    assert r_post.status_code == 200