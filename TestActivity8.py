# import statements

import unittest
import activity8




class CustomerInfo(unittest.TestCase):


    def test_find_customer_1000(self):
        result = activity8.find_customer(str(1000))
        expected_result = 'No customer with that specified ID.'
        self.assertMultiLineEqual(expected_result, result)


    def test_find_customer_101(self):
        result = activity8.find_customer(str(101))
        expected_firstname = 'James'
        expected_lastname = 'Butler'
        expected_address = '6649 N Blue Gum St'
        self.assertMultiLineEqual(expected_firstname, result.firstName)
        self.assertMultiLineEqual(expected_lastname, result.lastName)
        self.assertMultiLineEqual(expected_address, result.address)

    def test_find_customer_200(self):
        result = activity8.find_customer(str(200))
        expected_firstname = 'Arlene'
        expected_lastname = 'Klusman'
        expected_address = '3 Secor Rd'
        self.assertMultiLineEqual(expected_firstname, result.firstName)
        self.assertMultiLineEqual(expected_lastname, result.lastName)
        self.assertMultiLineEqual(expected_address, result.address)

    def test_find_customer_300(self):
        result = activity8.find_customer(str(300))
        expected_firstname = 'Jolanda'
        expected_lastname = 'Hanafan'
        expected_address = '37855 Nolan Rd'
        self.assertMultiLineEqual(expected_firstname, result.firstName)
        self.assertMultiLineEqual(expected_lastname, result.lastName)
        self.assertMultiLineEqual(expected_address, result.address)


    def test_find_customer_novalue(self):
        result = activity8.find_customer(str( ))
        expected_result = 'No customer with that specified ID.'
        self.assertMultiLineEqual(expected_result, result)

    def test_find_customer_negative(self):
        result = activity8.find_customer(str(-500))
        expected_result = 'No customer with that specified ID.'
        self.assertMultiLineEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()





