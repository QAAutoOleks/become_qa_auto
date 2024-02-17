import pytest
import sqlite3
from datetime import date
from modules.common.database import Database


@pytest.mark.database
def test_database_connection(database_tests):
    database_tests.testing_connection()

@pytest.mark.database
def test_check_all_customers(database_tests):
    users = database_tests.get_all_customers()

    print(users)

@pytest.mark.database
def test_check_customer_sergii(database_tests):
    user = database_tests.get_customer_adress_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_insert_and_delete_customer(database_tests):
    initially_length_of_customers_list = len(
        database_tests.get_all_customers())
    database_tests.insert_customer(
        50, 'Pavlo', 'Poshtova str, 32', 'Kharkiv', '61000', 'Ukraine')
    final_length_of_customers_list = len(
        database_tests.get_all_customers())
    assert final_length_of_customers_list == initially_length_of_customers_list + 1
    database_tests.delete_customer(50)

@pytest.mark.database
def test_insert_customer_with_id_not_unique(database_tests):
    database_tests.insert_customer(
        50, 'Pavlo', 'Poshtova str, 32', 'Kharkiv', '61000', 'Ukraine')
    try:
        database_tests.insert_customer(
            50, 'Pavlo', 'Poshtova str, 32', 'Kharkiv', '61000', 'Ukraine')
    except sqlite3.IntegrityError as e:
        assert str(e) == 'UNIQUE constraint failed: customers.id'
    database_tests.delete_customer(50)

@pytest.mark.database
def test_update_customer(database_tests):
    database_tests.update_customers_data('city', 'Dnipro', 2)
    assert database_tests.get_info_about_customer('city', 2) == [('Dnipro',)]
    database_tests.update_customers_data('postalCode', '49000', 2)
    assert database_tests.get_info_about_customer('postalCode', 2) == [('49000',)]

@pytest.mark.database
def test_update_quantity_of_products(database_tests):
    database_tests.update_quantity_of_products(25, 1)

    assert database_tests.get_quantity_products(1)[0][0] == 25

@pytest.mark.database
def test_insert_product(database_tests):
    database_tests.insert_product(11, 'печиво', 'солодке', 30)
    assert database_tests.get_product_by_id(11)[0][0] == 30

@pytest.mark.database
def test_insert_and_delete_product(database_tests):
    database_tests.insert_product(20, 'test', 'data', 999)
    assert database_tests.get_product_by_id(20) == [(999.0,)]
    
    database_tests.delete_product(20)
    assert database_tests.get_product_by_id(20) == []

@pytest.mark.database
def test_insert_valid_data_in_table_orders(database_tests):
    date_today = str(date.today())
    database_tests.insert_in_orders_data()
    assert len(
        database_tests.get_list_of_data_orders()) == 6
    assert database_tests.get_list_of_data_orders()[0][4] == date_today
    assert len(
        database_tests.get_orders_inner_join_customers_and_products_by_name_of_product(
            'солодка вода'
        )) == 4
    assert database_tests.get_orders_inner_join_customers_and_products_by_name_of_product(
            'молоко'
        )[0] == ('молоко', 1.5, date_today, 'Sergii', 'натуральне незбиране')
    assert (len(database_tests.get_orders_inner_join_customers_and_products_by_name_of_customer(
        'Sergii'
        ))) == 3
    assert (database_tests.get_orders_inner_join_customers_and_products_by_name_of_customer(
        'Sergii'
        ))[0] == ('Sergii', 'солодка вода', 3.5, date_today, 'з цукром')

@pytest.mark.database
def test_delete_order(database_tests):
    database_tests.delete_order(4)
    assert database_tests.get_order_by_id(4) == []

@pytest.mark.database
def test_insert_invalid_data_types_in_order(database_tests):
    with pytest.raises(Exception) as excinfo:
        database_tests.insert_product(11, 'печиво', 'солодке', 'Thirty')

    assert "no such column: Thirty" in str(excinfo.value)

@pytest.mark.database
def test_insert_order_when_quantity_of_products_not_enough(database_tests):
    with pytest.raises(Exception) as excinfo:
        database_tests.insert_in_orders_method('солодка вода', 30, 1, 1)

    assert 'CHECK constraint failed: quantity >= 0' in str(excinfo.value)