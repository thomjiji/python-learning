import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """
    Use setUp() method to create a instance of Employee class.
    Add self to the beginning of the instance, so this instance
    can be used in other method below.
    """

    def setUp(self):
        self.employee_one = Employee('Kendrick', 'Lamar', 100)

    def test_give_default_raise(self):
        self.employee_one.get_raise()

    def test_give_custom_raise(self):
        self.employee_one.get_raise(100)


if __name__ == '__main__':
    unittest.main()