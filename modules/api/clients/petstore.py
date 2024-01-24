import pytest
import requests


class PetStore:

    id = 0

    def __init__(self):
        PetStore.id += 1
        self.id = PetStore.id
        self.url_pets = 'https://petstore.swagger.io/v2/pet/'

    def post_pet_method(self, name_category, name_of_pet):
        body = {
            "id": self.id,
            "category": {"id": self.id, "name": name_of_pet},
            "name": name_category,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r_post = requests.post(self.url_pets, json=body)

    def put_pet_method(self, new_name):
        body = {
            "id": self.id,
            "category": {"id": self.id, "name": new_name},
            "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r_put = requests.put(self.url_pets, json=body)

    def get_pet_by_id(self, id):
        r_get_pet_by_id = requests.get(self.url_pets + str(id))
        r_get_pet_by_id_json = r_get_pet_by_id.json()
        
        return r_get_pet_by_id_json

    def create_list_of_users_with_array(self):
        body = [
            {
                "id": self.id,
                "username": "BobDylan",
                "firstName": "Bob",
                "lastName": "Dylan",
                "email": "bob.dylan@mail.com",
                "password": "123",
                "phone": "9999876543",
                "userStatus": 0,
            },
            {
                "id": self.id + 1,
                "username": "JohnConnor",
                "firstName": "John",
                "lastName": "Connor",
                "email": "john.connor.dylan@mail.com",
                "password": "123",
                "phone": "9999870043",
                "userStatus": 0,
            },
        ]
        self.r_create_list_of_users = requests.post(
            self.base_url + "createWithArray", json=body
        )

    def get_user(self, user_name):
        self.r_get_user = requests.get(self.base_url + user_name).json()

    def login_user(self, login, password):
        self.r_login_user = requests.get(
            self.base_url + "login", params={"username": login, "password": password}
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


