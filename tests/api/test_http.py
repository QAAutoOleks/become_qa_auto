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
    print(f"Response Body is {r.json()}")
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers are {r.headers}")