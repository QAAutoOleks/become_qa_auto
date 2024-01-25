import pytest


# @pytest.mark.api_git
# def test_user_exists(github_api):
#     user = github_api.get_user('defunkt')
#     assert user['login'] == 'defunkt'

# @pytest.mark.api_git
# def test_user_not_exists(github_api):
#     user = github_api.get_user('seergiybutenko')
#     assert user['message'] == 'Not Found'

# @pytest.mark.api_git
# def test_repo_can_be_found(github_api):
#     repo = github_api.search_repo('become-qa-auto')
#     assert repo['total_count'] == 54
#     assert 'become-qa-auto' in repo['items'][0]['name']

# @pytest.mark.api_git
# def test_repo_cannot_be_found(github_api):
#     repo = github_api.search_repo('become-qa-auto_oleksandr')
#     assert repo['total_count'] == 0

# @pytest.mark.api_git
# def test_repo_with_single_char_be_found(github_api):
#     repo = github_api.search_repo('b')
#     assert repo['total_count'] != 0

# @pytest.mark.api_git
# def test_get_list_of_branches(github_api):
#     list_repo = github_api.get_list_branches('QAAutoOleks', 'python_basics')
#     assert len(list_repo) == 4

# @pytest.mark.api_git
# def test_get_branch(github_api):
#     assert github_api.get_branch(
#         'QAAutoOleks', 'python_basics', 'main'
#     )['name'] == 'main' and github_api.get_branch(
#         'QAAutoOleks', 'python_basics', 'main'
#     )['commit']['commit']['author']['name'] == 'Oleksandr Tsupko'

@pytest.mark.api_git
def test_emoji(github_api):
    github_api.get_emogjis() == 200

@pytest.mark.api_git
def test_get_commit(github_api):
    assert github_api.get_commits('QAAutoOleks', 'python_basics')[0]['commit']['author']['name'] == 'Oleksandr Tsupko'
    assert github_api.get_commits('QAAutoOleks', 'pythonbasics')['message'] == 'Not Found'
