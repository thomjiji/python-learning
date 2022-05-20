class User:
    def __init__(self, fname, lname, age, location):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.location = location
        self.login_attempt = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old, and based on {self.location}.")

    def greet_user(self):
        print(f"Good morning! {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0


class Admin(User):
    def __init__(self, fname, lname, age, location):
        super().__init__(fname, lname, age, location)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"Administrator's privileges contains: ")
        for i in self.privileges:
            num = self.privileges.index(i) + 1
            print(num, '. ', i, sep='')
            num += 1