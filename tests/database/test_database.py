import pytest
import sqlite3
from datetime import date
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.testing_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_adress_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_update_quantity_of_products():
    db = Database()
    db.update_quantity_of_products('з цукром', 25)

    assert db.get_quantity_products('з цукром')[0][0] == 25

@pytest.mark.database
def test_create_new_product():
    db = Database()
    db.create_new_product(11, 'печиво', 'солодке', 30)
    assert db.get_product_by_id(11)[0][0] == 30

@pytest.mark.database
def test_create_and_delete():
    db = Database()
    db.create_new_product(20, 'test', 'data', 999)
    # db.delete_product(20)
    # assert db.get_product_by_id(20) == []

@pytest.mark.database
def test_insert_valid_data_in_table_orders():
    db = Database()
    db.insert_in_orders_data()
    assert len(db.get_list_of_data_orders()) == 6
    assert db.get_list_of_data_orders()[0][4] == str(date.today())
    assert len(
        db.get_orders_inner_join_customers_and_products_by_name_of_product(
            'солодка вода'
        )) == 4
    assert db.get_orders_inner_join_customers_and_products_by_name_of_product(
            'молоко'
        )[0] == ('молоко', 1.5, '2024-01-26', 'Sergii', 'натуральне незбиране')
    assert (len(db.get_orders_inner_join_customers_and_products_by_name_of_customer(
        'Sergii'
        ))) == 3
    assert (db.get_orders_inner_join_customers_and_products_by_name_of_customer(
        'Sergii'
        ))[0] == ('Sergii', 'солодка вода', 3.5, '2024-01-26', 'з цукром')

@pytest.mark.database
def test_insert_invalid_data_types():
    db = Database()
    try:
        db.create_new_product(11, 'печиво', 'солодке', 'Thirty')
    except sqlite3.OperationalError as e:
        assert str(e) == "no such column: Thirty"
