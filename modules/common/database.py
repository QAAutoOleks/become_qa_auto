import sqlite3
from datetime import date


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:\\Users\\User\\Desktop\\become_qa_auto" + r"\\become_qa_auto.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("DROP TABLE IF EXISTS orders")
        modificate_table_orders = """CREATE TABLE orders (
            id_orders INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name_of_product VARCHAR(255) NOT NULL,
            quantity_of_product REAL NOT NULL,
            date_of_order VARCHAR(255) NOT NULL,
            customers_id INTEGER,
            products_id INTEGER,
            FOREIGN KEY (customers_id) REFERENCES customers (id)
            FOREIGN KEY (products_id) REFERENCES products (id)
        )"""
        self.cursor.execute(modificate_table_orders)

        Database.update_quantity_of_products(self, 20, 1)
        Database.update_quantity_of_products(self, 20, 2)
        Database.update_quantity_of_products(self, 20, 3)

        self.cursor.execute("DROP TABLE IF EXISTS temporary_products")
        modificate_table_products = """CREATE TABLE temporary_products (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(255) NOT NULL,
            quantity REAL NOT NULL CHECK (quantity >= 0)
        )"""
        self.cursor.execute(modificate_table_products)

        new_table_products = """INSERT INTO temporary_products
        SELECT * FROM products"""
        self.cursor.execute(new_table_products)
        self.connection.commit()

        self.cursor.execute("DROP TABLE IF EXISTS products")
        old_table_products = """ALTER TABLE temporary_products 
            RENAME TO products"""
        self.cursor.execute(old_table_products)
        self.connection.commit()

        
    def get_list_of_data_orders(self):
        query = f"SELECT \
            orders.id_orders, \
            customers.id, \
            products.name, \
            products.description, \
            orders.date_of_order\
            FROM orders\
            JOIN customers ON orders.customers_id = customers.id\
            JOIN products ON orders.products_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_orders_inner_join_customers_and_products_by_name_of_product(self, product_name):
        sql = f"""SELECT 
            name_of_product, 
            quantity_of_product, 
            date_of_order, 
            customers.name,
            products.description 
            FROM orders 
            INNER JOIN customers 
            ON orders.customers_id = customers.id 
            INNER JOIN products 
            ON products.id = orders.products_id
            WHERE products.name = '{product_name}';"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    def get_orders_inner_join_customers_and_products_by_name_of_customer(self, customer_name):
        sql = f"""SELECT 
            customers.name,
            products.name,
            orders.quantity_of_product, 
            orders.date_of_order,
            products.description 
            FROM customers 
            INNER JOIN orders 
            ON customers.id = orders.customers_id 
            INNER JOIN products 
            ON products.id = orders.products_id
            WHERE customers.name = '{customer_name}';"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    def testing_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_customers(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_customer_adress_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_customer(self, id, name, address, city, postalCode, country):
        query = f"INSERT INTO customers (\
            id, name, address, city, postalCode, country) \
            VALUES ({id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def update_customers_data(self, modification_attribute, new_city, customer_id):
        query = f"UPDATE customers SET '{modification_attribute}' = '{new_city}' \
            WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_customer(self, customer_id):
        query = f"DELETE FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_info_about_customer(self, required_attribute, customer_id):
        query = f"SELECT {required_attribute} FROM customers \
            WHERE id = {customer_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def update_quantity_of_products(self, quantity, id):
        query = f"UPDATE products SET quantity = {quantity} WHERE id = '{id}'"
        self.cursor.execute(query)
        self.connection.commit()

    def get_quantity_products(self, id):
        query = f"SELECT quantity FROM products WHERE id = '{id}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_product_by_id(self, id):
        query = f"SELECT quantity FROM products WHERE id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def insert_product(self, id, name, description, quantity):
        query = f"INSERT OR REPLACE INTO products \
            (id, name, description, quantity) \
            VALUES ({id}, '{name}', '{description}', {quantity})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product(self, id):
        query = f"DELETE FROM products WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_in_orders_method(self, name_of_product, quantity_of_product, customers_id, products_id):
        date_today = str(date.today())
        query = f"INSERT OR REPLACE INTO orders \
            (name_of_product, quantity_of_product, \
                date_of_order, customers_id, products_id) \
            VALUES ('{name_of_product}', '{quantity_of_product}', \
                '{date_today}', '{customers_id}', '{products_id}')"
        self.cursor.execute(query)
        self.connection.commit()

        quantity_of_product_after_new_order_created = Database.get_quantity_products(
            self, products_id)[0][0]
        quantity_of_product_after_new_order_created -= quantity_of_product
        quantity_of_product_after_new_order_created = str(
            quantity_of_product_after_new_order_created)
        Database.update_quantity_of_products(
            self, quantity_of_product_after_new_order_created, products_id)

    def insert_in_orders_data(self):
        Database.insert_in_orders_method(self, 'солодка вода', 3.5, 1, 1)
        Database.insert_in_orders_method(self, 'солодка вода', 2, 1, 2)
        Database.insert_in_orders_method(self, 'молоко', 1.5, 1, 3)
        Database.insert_in_orders_method(self, 'солодка вода', 5, 2, 1)
        Database.insert_in_orders_method(self, 'солодка вода', 1, 2, 2)
        Database.insert_in_orders_method(self, 'молоко', 2, 2, 3)

    def get_order_by_id(self, order_id):
        query = f"SELECT name_of_product FROM orders WHERE id_orders = {order_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def delete_order(self, order_id):
        query = f"DELETE FROM orders WHERE id = {order_id}"
