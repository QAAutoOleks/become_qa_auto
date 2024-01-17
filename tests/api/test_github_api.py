import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api_git
def test_user_exists():
    api = GitHub()
    user = api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api_git
def test_user_not_exists():
    api = GitHub()
    user = api.get_user('seergiybutenko')
    assert user['message'] == 'Not Found'