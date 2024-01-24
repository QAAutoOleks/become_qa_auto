import pytest


@pytest.mark.api_petstore
def test_check_post(pet_crud):
    pet_crud.post_pet_method("Dogs", "Chihuahua")
    pet_crud.put_pet_method("Boxer")
    assert pet_crud.get_pet_by_id(1)['category']['name'] == 'Boxer'
    #assert pet_crud.r_post.status_code == 200    

# @pytest.mark.api_petstore    
# def test_check_put(pet_crud):
#     assert pet_crud.r_put.status_code == 200

# @pytest.mark.api_petstore
# def test_get_by_id(pet_crud):
#     assert pet_crud.r_get_by_id['category']['name'] == 'Mazik'

# @pytest.mark.api_petstore
# def test_id(pet_crud):
#     assert pet_crud.id == 4

# @pytest.mark.api_petstore
# def test_create_list_of_user_with_array(user_crud):
#     assert user_crud.r_get_user['username'] == 'BobDylan'
#     # 'id' is joint with 'pet_crud'
#     assert user_crud.id == 5
#     assert user_crud.r_login_user.status_code == 200

# @pytest.mark.api_petstore
# def test_store(store_crud):
#     assert store_crud.r_get_order.json()['quantity'] == 2
