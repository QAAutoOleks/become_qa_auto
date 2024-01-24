import pytest
import requests


class PetStore:

    pet_id = 0
    user_id = 0
    order_id = 0

    def __init__(self):
        self.url_pets = 'https://petstore.swagger.io/v2/pet/'
        self.url_user = 'https://petstore.swagger.io/v2/user/'
        self.url_store = 'https://petstore.swagger.io/v2/store/order'

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
        r_post = requests.post(self.url_pets, json=body)

        return r_post.status_code

    def put_pet(self, new_name):
        body = {
            "id": self.pet_id,
            "category": {"id": 0, "name": new_name},
            "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        r_put = requests.put(self.url_pets, json=body)

        return r_put.status_code

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

    def put_user_change_email(self, username, new_email):
        body = self.get_user(username)
        body['email'] = new_email

        r_put_user = requests.put(self.url_user + username, json=body)

        return r_put_user.status_code

    def get_user(self, username):
        r_get_user = requests.get(self.url_user + username)

        return r_get_user.json()

    def login_user(self, login, password):
        r_login_user = requests.get(
            # self.url_user + "login", params={"username": login, "password": password}
            self.url_user + "login?username={login}&password={password}"
        )

        return r_login_user.status_code

    def post_order(self, quantity):
        PetStore.order_id += 1
        self.order_id = PetStore.order_id

        body = {
            "id": self.order_id,
            "petId": 0,
            "quantity": quantity,
            "shipDate": "2024-01-24T15:17:12.176Z",
            "status": "placed",
            "complete": True,
        }
        post_order = requests.post(self.url_store, json=body)

        return post_order.status_code

    def get_order(self, order_id):
        r_get_order = requests.get(
            self.url_store + '/' + str(order_id))

        return r_get_order.json()

    def delete_order(self, order_id):
        r_delete_order = requests.delete(self.url_store + '/' + str(order_id))

        return r_delete_order.status_code
