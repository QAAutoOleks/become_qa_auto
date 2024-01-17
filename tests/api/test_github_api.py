import pytest


@pytest.mark.api_git
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api_git
def test_user_not_exists(github_api):
    user = github_api.get_user('seergiybutenko')
    assert user['message'] == 'Not Found'

@pytest.mark.api_git
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo('become-qa-auto')
    assert repo['total_count'] == 54
    assert 'become-qa-auto' in repo['items'][0]['name']

@pytest.mark.api_git
def test_repo_cannot_be_found(github_api):
    repo = github_api.search_repo('become-qa-auto_oleksandr')
    assert repo['total_count'] == 0