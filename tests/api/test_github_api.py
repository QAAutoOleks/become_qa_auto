import pytest


@pytest.mark.api_git
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api_git
def test_user_not_exists(github_api):
    user = github_api.get_user('seergiybutenko')
    assert user['message'] == 'Not Found'