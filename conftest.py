import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.petstore import PetStore
from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from modules.ui.page_objects.rozetka_laptops_page import RozetkaLaptopsPage
from modules.ui.page_objects.rozetka_goods_page import RozetkaGoodsPage
from modules.common.database import Database


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
    pet_store = PetStore()

    yield pet_store


@pytest.fixture
def rozetka_main_page():
    rozetka_main_page = RozetkaMainPage()

    yield rozetka_main_page


@pytest.fixture
def rozetka_laptops_page():
    rozetka_laptops_page = RozetkaLaptopsPage()

    yield rozetka_laptops_page


@pytest.fixture
def rozetka_goods_page():
    rozetka_goods_page = RozetkaGoodsPage()

    yield rozetka_goods_page

@pytest.fixture
def database_tests():
    database = Database()

    yield database