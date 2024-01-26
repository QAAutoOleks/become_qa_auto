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


@pytest.mark.api_git
def test_repo_with_single_char_be_found(github_api):
    repo = github_api.search_repo('b')
    assert repo['total_count'] != 0


@pytest.mark.api_git
def test_emoji(github_api):
    assert github_api.get_emogjis().status_code == 200
    assert len(github_api.get_emogjis().json()) == 1877


@pytest.mark.api_git
def test_get_commit(github_api):
    assert github_api.get_commits('QAAutoOleks', 'python_basics')[
        0]['commit']['author']['name'] == 'Oleksandr Tsupko'
    assert github_api.get_commits('QAAutoOleks', 'pythonbasics')[
        'message'] == 'Not Found'


@pytest.mark.api_git
def test_get_commits_by_sha(github_api):
    sha = 'eeecaa1c28bd344becf888de1f9d82aec85bcb27'
    assert github_api.get_list_commits(
        'QAAutoOleks', 'python_basics', sha
    )[0]['commit']['url'] == f'https://api.github.com/repos/QAAutoOleks/python_basics/commits/{sha}'


@pytest.mark.api_git
def test_get_list_of_branches(github_api):
    list_repo = github_api.get_list_branches('QAAutoOleks', 'python_basics')
    assert len(list_repo) == 4


@pytest.mark.api_git
def test_get_branch(github_api):
    assert github_api.get_branch(
        'QAAutoOleks', 'python_basics', 'main'
    )['name'] == 'main' and github_api.get_branch(
        'QAAutoOleks', 'python_basics', 'main'
    )['commit']['commit']['author']['name'] == 'Oleksandr Tsupko'


@pytest.mark.api_git
def test_get_content_from_directory(github_api):
    print(github_api.get_content_from_directory(
        'QAAutoOleks', 'python_basics', 'Lessons'
    )[0]['html_url']) == 'https://github.com/QAAutoOleks/python_basics/blob/main/Lessons/assign_1.py'
