import pg8000

class BusinessLayer:
    def __init__(self, server, database, user, password):
        self.connection_string = {
            "host": server,
            "database": database,
            "user": user,
            "password": password
        }

    def connect(self):
        try:
            self.connection = pg8000.connect(**self.connection_string)
            self.cursor = self.connection.cursor()
        except Exception as e:
            raise Exception(f"Database connection failed: {e}")

    def count_in450a(self):
        self.cursor.execute("SELECT COUNT(*) FROM IN450a;")
        return self.cursor.fetchone()[0]

    def get_in450b_names(self):
        self.cursor.execute("SELECT first_name, last_name FROM IN450b;")
        return self.cursor.fetchall()

    def count_in450c(self):
        self.cursor.execute("SELECT COUNT(*) FROM IN450c;")
        return self.cursor.fetchone()[0]

    def close(self):
        self.cursor.close()
        self.connection.close()
