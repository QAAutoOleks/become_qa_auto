import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:\\Users\\User\\Desktop\\Framework\\Become-QA-Auto" + r"\\become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_adress_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_quantity_of_products(self, description, quantity):
        query = f"UPDATE products SET quantity = {quantity} WHERE description = '{description}'"
        self.cursor.execute(query)
        self.connection.commit() # підтвердження змін в базі даних

    def get_quantity_products(self, products_description):
        query = f"SELECT quantity FROM products WHERE description = '{products_description}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_product_by_id(self, id):
        query = f"SELECT quantity FROM products WHERE id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def create_new_product(self, id, name, description, quantity):
        query = f"INSERT OR REPLACE INTO products \
            (id, name, description, quantity) \
            VALUES ({id}, '{name}', '{description}', {quantity})"
        self.cursor.execute(query)
        self.connection.commit()
        new_product = Database.get_product_by_id(self, id)
        return new_product

    def delete_product(self, id):
        query = f"DELETE FROM products WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit

    def get_list_of_data(self):
        query = f"SELECT \
            orders.id, \
            customers.id, \
            products.name, \
            products.description, \
            orders.order_date\
                FROM orders\
                    JOIN customers ON orders.customer_id = customers.id\
                        JOIN products ON orders.product_id = products.id"
                            #WHERE description = '{data}'"               
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record