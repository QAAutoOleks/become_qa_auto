import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            'https://api.github.com/search/repositories',
            params={'q': name}
        )
        body = r.json()

        return body
        
    def get_emogjis(self):
        r = requests.get('https://api.github.com/emojis')

        return r

    def get_commits(self, owner, name_repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{name_repo}/commits')

        return r.json()

    def get_list_branches(self, owner, name_repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{name_repo}/branches')

        return r.json()

    def get_branch(self, owner, name_repo, name_branch):
        r = requests.get(f'https://api.github.com/repos/{owner}/{name_repo}/branches/{name_branch}')

        return r.json()

    def get_list_commits(self, owner, name_repo, SHA):
        r = requests.get(f'https://api.github.com/repos/{owner}/{name_repo}/commits/{SHA}/branches-where-head')

        return r.json()

    def get_content_from_directory(self, owner, name_repo, path=''):
        r = requests.get(f'https://api.github.com/repos/{owner}/{name_repo}/contents/{path}')

        return r.json()