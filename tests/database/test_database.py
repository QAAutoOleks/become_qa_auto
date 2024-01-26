import pytest
from modules.common.database import Database


# @pytest.mark.database
# def test_database_connection():
#     db = Database()
#     db.test_connection()

# @pytest.mark.database
# def test_check_all_users():
#     db = Database()
#     users = db.get_all_users()

#     print(users)

# @pytest.mark.database
# def test_check_user_sergii():
#     db = Database()
#     user = db.get_user_adress_by_name('Sergii')

#     assert user[0][0] == 'Maydan Nezalezhnosti 1'
#     assert user[0][1] == 'Kyiv'
#     assert user[0][2] == '3127'
#     assert user[0][3] == 'Ukraine'

# @pytest.mark.database
# def test_update_quantity_of_products():
#     db = Database()
#     db.update_quantity_of_products('з цукром', 25)    

#     assert db.get_quantity_products('з цукром')[0][0] == 25

# @pytest.mark.database
# def test_create_new_product():
#     db = Database()
#     # в результаті отримуємо tuple
#     assert db.create_new_product(11, 'печиво', 'солодке', 30)[0][0] == 30

# @pytest.mark.database
# def test_create_and_delete():
#     db = Database()
#     db.create_new_product(20, 'test', 'data', 999)
#     db.delete_product(20)
#     assert db.get_product_by_id(20) == []

# @pytest.mark.database
# def test_list_of_data():
#     db = Database()
#     assert db.get_list_of_data()[0][0] == 1
#     assert db.get_list_of_data()[0][1] == 1
#     assert db.get_list_of_data()[0][2] == 'солодка вода'
#     assert db.get_list_of_data()[0][3] == 'з цукром'

@pytest.mark.database
def test_create_new_table():
    db = Database()