import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.petstore import PetStore


class User:

    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Sergii'
        self.second_name = 'Butenko'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()

    yield api


@pytest.fixture
def petstore_api():
    first_pet = PetStore()

    yield first_pet


@pytest.fixture
def store_crud():
    first_store = PetStore("https://petstore.swagger.io/v2/store/")
    first_store.post_method("Dogs", "Fur")
    first_store.post_order()
    first_store.get_order()

    yield first_store
