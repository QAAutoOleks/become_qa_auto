import requests


class GitHub:

    def get_user_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body

    def get_user_non_exist_user(self):
        r = requests.get('https://api.github.com/users/seergiybutenko')
        body = r.json()

        return body