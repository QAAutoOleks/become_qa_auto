import pytest


@pytest.mark.api_petstore
def test_check_post(petstore_api):
    petstore_api.post_pet("Dogs", "Chihuahua")
    assert petstore_api.get_pet_by_id(1)['category']['name'] == 'Chihuahua'

    petstore_api.put_pet("Boxer")
    assert petstore_api.get_pet_by_id(1)['category']['name'] == 'Boxer'

    assert petstore_api.delete_pet(1) == 200
    assert petstore_api.get_pet_by_id(1)['message'] == 'Pet not found'

    petstore_api.post_pet("Cats", "Bengal")
    petstore_api.post_pet("Cats", "Persian")
    petstore_api.post_pet("Cats", "Scottish Fold")
    assert petstore_api.get_pet_by_id(4)['category']['name'] == 'Scottish Fold'

@pytest.mark.api_petstore
def test_create_list_of_user_with_array(petstore_api):
    assert petstore_api.create_list_of_users_with_array() == 200
    #assert user_crud.r_get_user['username'] == 'BobDylan'
#     # 'id' is joint with 'pet_crud'
#     assert user_crud.id == 5
#     assert user_crud.r_login_user.status_code == 200

# @pytest.mark.api_petstore
# def test_store(store_crud):
#     assert store_crud.r_get_order.json()['quantity'] == 2
