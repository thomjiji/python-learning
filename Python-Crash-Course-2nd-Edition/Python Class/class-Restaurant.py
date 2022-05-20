class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} type of cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, people):
        self.number_served += people


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['Apple', 'Bacon', 'Beer', 'Blue moon']

    def display_flavors(self):
        print(f"{self.restaurant_name} has these flavors of ice cream: ")
        for item in self.flavors:
            print('-', item)


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


# # 9-1
# restaurant1 = Restaurant('帝豪大酒店', 341)
# print(restaurant1.restaurant_name)
# print(restaurant1.cuisine_type)
# restaurant1.open_restaurant()
# restaurant1.describe_restaurant()

# # 9-2
# restaurant2 = Restaurant('亚朵酒店', 31)
# restaurant2.describe_restaurant()

# # 9-3
# user_1 = User('Thom', 'Yorke', 56, 'New York City')
# print(user_1.first_name)
# print(user_1.last_name)
# user_1.describe_user()
# user_1.greet_user()

# # 9-4. Number Served
# restaurant3 = Restaurant('Noma', 90)
#
# restaurant3.number_served = 10000
# print(restaurant3.number_served)
#
# restaurant3.set_number_served(10)
# print(restaurant3.number_served)
#
# restaurant3.increment_number_served(10)
# print(restaurant3.number_served)

# # 9.5. Login Attempts
# user_2 = User('huang', 'erzhi', 24, 'Beijing')
# user_2.describe_user()
#
# user_2.increment_login_attempts()
# user_2.increment_login_attempts()
# user_2.increment_login_attempts()
# print(user_2.login_attempt)
#
# user_2.reset_login_attempts()
# print(user_2.login_attempt)

# # 9-6 Ice Cream Stand
# my_ice_cream = IceCreamStand("冰淇淋展台", 89)
# my_ice_cream.display_flavors()

# 9-7 Admin
my_admin = Admin('Donald', 'Trump', 75, 'Mar-a-Lago')
my_admin.privileges.show_privileges()