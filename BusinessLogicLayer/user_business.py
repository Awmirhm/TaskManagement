from DataAccessLayer.user_data_access import UserDataAccess
from passlib.hash import pbkdf2_sha256


class UserBusiness:
    def __init__(self):
        self.user_data_access = UserDataAccess()

        self.user = None

    def sign_in(self, firstname, lastname, username, password):
        usernames = self.user_data_access.return_all_username()

        if len(firstname) < 3:
            return [None, "Length should be least 3"]
        if any(char.isdigit() for char in firstname):
            return [None, "The First Name does not have a number"]

        if len(lastname) < 4:
            return [None, "Length should be least 4"]
        if any(char.isdigit() for char in lastname):
            return [None, "The Last Name does not have a number"]

        if len(username) < 3:
            return [None, "Length should be least 3"]
        for item in usernames:
            if username == item:
                return [None, "Duplicate Username"]

        if len(password) < 6:
            return [None, "length should be at least 6"]
        if len(password) > 20:
            return [None, "length should be not be greater than 20"]
        if not any(char.isdigit() for char in password):
            return [None, "Password should have at least one numeral"]
        if not any(char.isupper() for char in password):
            return [None, "Password should have at least one uppercase letter"]
        if not any(char.islower() for char in password):
            return [None, "Password should have at least one lowercase letter"]

        hash_password = pbkdf2_sha256.hash(password)

        self.user_data_access.create_account(firstname, lastname, username, hash_password)
        return [f"You have successfully registered in the application.\n Go back to the previous page and login.", None]

    def login(self, username, password):
        passwords = self.user_data_access.return_all_password()

        if len(username) < 3 or len(password) < 3:
            return [None, "Invalid Access"]
        else:
            for item in passwords:
                if pbkdf2_sha256.verify(password, item):
                    self.user = self.user_data_access.get_user(username, item)
                    break

            if self.user:
                return [self.user, None]
            else:
                return [None, "Invalid Username or Password"]

    def set_meter_size(self, meter, current_user):
        self.user_data_access.set_meter(meter, current_user.id)

    def get_meter_size(self, current_user):
        meter_size = self.user_data_access.get_meter_size(current_user.id)
        if meter_size:
            return [meter_size, None]
        else:
            return [None, "Invalid"]
