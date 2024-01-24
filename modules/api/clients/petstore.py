import pytest
import requests


class PetStore:

    pet_id = 0
    user_id = 0

    def __init__(self):
        self.url_pets = 'https://petstore.swagger.io/v2/pet/'
        self.url_user = 'https://petstore.swagger.io/v2/user/'
        self.url_store = 'https://petstore.swagger.io/v2/store/'

    def post_pet(self, name_category, name_of_pet):
        PetStore.pet_id += 1
        self.pet_id = PetStore.pet_id

        body = {
            "id": self.pet_id,
            "category": {"id": 0, "name": name_of_pet},
            "name": name_category,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r_post = requests.post(self.url_pets, json=body)

    def put_pet(self, new_name):
        body = {
            "id": self.pet_id,
            "category": {"id": 0, "name": new_name},
            "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r_put = requests.put(self.url_pets, json=body)

    def get_pet_by_id(self, id):
        r_get_pet = requests.get(self.url_pets + str(id))
        r_get_pet_json = r_get_pet.json()

        return r_get_pet_json

    def delete_pet(self, id):
        r_delete = requests.delete(self.url_pets + str(id))

        return r_delete.status_code
        

    def create_list_of_users_with_array(self):
        PetStore.user_id += 2
        self.user_id = PetStore.user_id

        body = [
            {
                "id": self.user_id,
                "username": "IvanFranko",
                "firstName": "Ivan",
                "lastName": "Franko",
                "email": "ivan.franko@mail.com",
                "password": "123",
                "phone": "9999876543",
                "userStatus": 0,
            },
            {
                "id": self.user_id - 1,
                "username": "HrygoriiSkovoroda",
                "firstName": "Hrygorii",
                "lastName": "Skovoroda",
                "email": "hrygorii.skovoroda@mail.com",
                "password": "123",
                "phone": "9999870043",
                "userStatus": 0,
            },
        ]
        r_create_list_of_users = requests.post(
            self.url_user + "createWithArray", json=body
        )

        return r_create_list_of_users.status_code

    def get_user(self, user_name):
        self.r_get_user = requests.get(self.url_user + user_name).json()

    def login_user(self, login, password):
        self.r_login_user = requests.get(
            self.url_user + "login", params={"username": login, "password": password}
        )

    def post_order(self):
        body = {
            "id": self.id,
            "petId": self.id,
            "quantity": 2,
            "shipDate": "2024-01-15T17:33:32.207Z",
            "status": "placed",
            "complete": True,
        }
        self.post_order = requests.post(self.base_url + "order", json=body)
    
    def get_order(self):
        self.r_get_order = requests.get(self.base_url + "order/" + str(self.id))


