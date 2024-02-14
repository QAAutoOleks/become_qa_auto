import pytest
import sqlite3
from datetime import date
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.testing_connection()

@pytest.mark.database
def test_check_all_customers():
    db = Database()
    users = db.get_all_customers()

    print(users)

@pytest.mark.database
def test_check_customer_sergii():
    db = Database()
    user = db.get_customer_adress_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_insert_and_delete_customer():
    db = Database()
    initially_length_of_customers_list = len(db.get_all_customers())
    db.insert_customer(50, 'Pavlo', 'Poshtova str, 32', 'Kharkiv', '61000', 'Ukraine')
    final_length_of_customers_list = len(db.get_all_customers())
    assert final_length_of_customers_list == initially_length_of_customers_list + 1
    db.delete_customer(50)

@pytest.mark.database
def test_insert_customer_with_id_not_unique():
    db = Database()
    db.insert_customer(50, 'Pavlo', 'Poshtova str, 32', 'Kharkiv', '61000', 'Ukraine')
    try:
        db.insert_customer(50, 'Pavlo', 'Poshtova str, 32', 'Kharkiv', '61000', 'Ukraine')
    except sqlite3.IntegrityError as e:
        assert str(e) == 'UNIQUE constraint failed: customers.id'
    db.delete_customer(50)

@pytest.mark.database
def test_update_customer():
    db = Database()
    db.update_customers_data('city', 'Dnipro', 2)
    assert db.get_info_about_customer('city', 2) == [('Dnipro',)]
    db.update_customers_data('postalCode', '49000', 2)
    assert db.get_info_about_customer('postalCode', 2) == [('49000',)]

@pytest.mark.database
def test_update_quantity_of_products():
    db = Database()
    db.update_quantity_of_products(25, 1)

    assert db.get_quantity_products(1)[0][0] == 25

@pytest.mark.database
def test_insert_product():
    db = Database()
    db.insert_product(11, 'печиво', 'солодке', 30)
    assert db.get_product_by_id(11)[0][0] == 30

@pytest.mark.database
def test_insert_and_delete_product():
    db = Database()
    db.insert_product(20, 'test', 'data', 999)
    assert db.get_product_by_id(20) == [(999.0,)]
    
    db.delete_product(20)
    assert db.get_product_by_id(20) == []

@pytest.mark.database
def test_insert_valid_data_in_table_orders():
    date_today = str(date.today())
    db = Database()
    db.insert_in_orders_data()
    assert len(db.get_list_of_data_orders()) == 6
    assert db.get_list_of_data_orders()[0][4] == date_today
    assert len(
        db.get_orders_inner_join_customers_and_products_by_name_of_product(
            'солодка вода'
        )) == 4
    assert db.get_orders_inner_join_customers_and_products_by_name_of_product(
            'молоко'
        )[0] == ('молоко', 1.5, date_today, 'Sergii', 'натуральне незбиране')
    assert (len(db.get_orders_inner_join_customers_and_products_by_name_of_customer(
        'Sergii'
        ))) == 3
    assert (db.get_orders_inner_join_customers_and_products_by_name_of_customer(
        'Sergii'
        ))[0] == ('Sergii', 'солодка вода', 3.5, date_today, 'з цукром')

@pytest.mark.database
def test_delete_order():
    db = Database()
    db.delete_order(4)
    assert db.get_order_by_id(4) == []

@pytest.mark.database
def test_insert_invalid_data_types_in_order():
    db = Database()
    try:
        db.insert_product(11, 'печиво', 'солодке', 'Thirty')
    except sqlite3.OperationalError as e:
        assert str(e) == "no such column: Thirty"

@pytest.mark.database
def test_insert_order_when_quantity_of_products_not_enough():
    db = Database()
    try:
        db.insert_in_orders_method('солодка вода', 30, 1, 1)
    except sqlite3.IntegrityError as e:
        assert str(e) == 'CHECK constraint failed: quantity >= 0'