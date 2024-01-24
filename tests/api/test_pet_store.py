import pytest


@pytest.mark.api_petstore
def test_check_post(petstore_api):
    assert petstore_api.post_pet("Dogs", "Chihuahua") == 200
    assert petstore_api.get_pet_by_id(1)['category']['name'] == 'Chihuahua'

    assert petstore_api.put_pet("Boxer") == 200
    assert petstore_api.get_pet_by_id(1)['category']['name'] == 'Boxer'

    assert petstore_api.delete_pet(1) == 200
    assert petstore_api.get_pet_by_id(1)['message'] == 'Pet not found'

    assert petstore_api.post_pet("Cats", "Bengal") == 200
    assert petstore_api.post_pet("Cats", "Persian") == 200
    assert petstore_api.post_pet("Cats", "Scottish Fold") == 200
    assert petstore_api.get_pet_by_id(4)['category']['name'] == 'Scottish Fold'

@pytest.mark.api_petstore
def test_create_list_of_user_with_array(petstore_api):
    assert petstore_api.create_list_of_users_with_array() == 200
    assert petstore_api.get_user('IvanFranko')['email'] == 'ivan.franko@mail.com'

    assert petstore_api.put_user_change_email('IvanFranko', 'ivan_franko@gmail.com') == 200
    assert petstore_api.get_user('IvanFranko')['email'] == 'ivan_franko@gmail.com'

    assert petstore_api.login_user('HrygoriiSkovoroda', '321') == 200

@pytest.mark.api_petstore
def test_store(petstore_api):
    assert petstore_api.post_order('a') == 500

    assert petstore_api.post_order(5) == 200
    assert petstore_api.get_order(2)['quantity'] == 5
    assert petstore_api.post_order(3) == 200
    assert petstore_api.get_order(3)['quantity'] == 3

    assert petstore_api.delete_order(-1) == 404
    assert petstore_api.delete_order(3) == 200
    assert petstore_api.get_order(3)['message'] == 'Order not found'
    

