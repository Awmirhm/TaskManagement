import sqlite3
from CommonLayer.user import User


class UserDataAccess:
    def __init__(self):
        self.data_base_name = "TaskManagement.db"

    def return_all_username(self):
        usernames = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       password
                FROM User""").fetchall()
            for item in data:
                usernames.append(item[3])
            return usernames

    def create_account(self, firstname, lastname, username, password):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    INSERT INTO User (
                             first_name,
                             last_name,
                             username,
                             password
                         )
                         VALUES (
                             ?,
                             ?,
                             ?,
                             ?
                         )
                        """, [firstname, lastname, username, password])
            connection.commit()

    def return_all_password(self):
        passwords = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       password
                FROM User""").fetchall()

            for item in data:
                passwords.append(item[4])
            return passwords

    def get_user(self, username, password):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       password,
                       meter
                FROM User
                WHERE  username = ?
                AND    password = ?""", [username, password]).fetchone()

            if data:
                user = User.create_with_tuple(data)
                return user
            else:
                return None

    def set_meter(self, meter, current_user_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    UPDATE User
                    SET    meter = ?
                    WHERE  id = ?""", [meter, current_user_id])

            connection.commit()

    def get_meter_size(self, user_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT meter
                    FROM User       
                    WHERE  id = ?""", [user_id]).fetchone()

            if data:
                meter = data[0]
                return meter
            else:
                return None
