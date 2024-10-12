# Task 1: Setup Testing Environment
# pip install unittest requests

# Task 2 and 3: Write Unit Tests for Each Endpoint with Mocking.
# TestEmployeeEndpoints (test_employee.py)
import unittest
from unittest.mock import patch
import requests

class TestEmployeeEndpoints(unittest. TestCase):

    @patch('app.models.Employee.query') # Mock database query
    def test_get_employee_success(self, mock_query):
        # Simulate a sucessfull employee retrieval
        mock_query.get.return_value = {'id': 1, 'name': 'Smith Alice'}
        response = requests.get('http://localhost:5000/employees/1')
        self.assertEqual(response.status.code, 200)
        self.assertEqual(response.json()['name'], 'Smith Alice')

    @patch('app.models.Employee.query') # Mock database query
    def test_get_employee_not_found(self, mock_query):
         # Simulate no employee found
        mock_query.get.return_value = None
        response = requests.get('http://localhost:5000/employees/999')
        self.assertEqual(response.status.code, 404)
    
    @patch('app.models.Employee.query')
    def test_create_employee_invalid_data(self, mock_query):
        # Test invalid data for creating an employee
        data = {'name': ''} # Invalid name
        response = requests.post('http://localhost:5000/employees/999', json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

# TestProductEndpoints (test_product.py)
import unittest
from unittest.mock import patch
import requests

class TestProductEndpoints(unittest. TestCase):

    @patch('app.models.Product.query')
    def test_get_product_success(self, mock_query):
        mock_query.get.return_value = {'id': 1, 'name': 'widget'}
        response = requests.get('http://localhost:5000/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'widget')

    @patch('app.models.Product.query')
    def test_get_product_not_found(self, mock_query):
        mock_query.get.return_value = None
        response = requests.get('http://localhost:5000/products/999')
        self.assertEqual(response.status_code, 404)
    
    @patch('app.models.Product.query')
    def test_create_product_invalid_data(self, mock_query):
        data = {'name': ''} # Invalid data
        response = requests.post('http://localhost:5000/products', json=data)
        self.assertEqual(response.status_code, 400)

if __name__== '__main__':
    unittest.main()

# TestOrderEndpoints (test_order.py)
import unittest
from unittest.mock import patch
import requests


class TestOrderEndpoints(unittest. TestCase):

    @patch('app.models.Order.query')
    def test_get_order_success(self, mock_query):
        mock_query.get.return_value = {'id': 1, 'customer_id': 101}
        response = requests.get('http://localhost:5000/orders/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['customer_id'], 101)

    @patch('app.models.Order.query')
    def test_get_order_not_found(self, mock_query):
        mock_query.get.return_value = None
        response = requests.get('http://localhost:5000/orders/999')
        self.assertEqual(response.status_code, 404)

    @patch('app.models.Order.query')
    def test_create_order_invalid_data(self, mock_query):
        data = {'customer_id': None} # Missing customer_id
        response = requests.post('http://localhost:5000/orders', json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

# TestCustomerEndpoints (test_customer.py)
import unittest
from unittest.mock import patch
import requests

class TestCustomerEndpoints(unittest.TestCase):

    @patch('app.models.Customer.query')
    def test_get_customer_success(self, mock_query):
        mock_query.get.return_value = {'id': 1, 'name': 'Alice'}
        response = requests.get('http://localhost:5000/customers/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Alice')

    @patch('app.models.Customer.query')
    def test_get_customer_not_found(self, mock_query):
        mock_query.get.return_value = None
        response = requests.get('http://localhost:5000/customers/999')
        self.assertEqual(response.status_code, 404)

    @patch('app.models.Customer.query')
    def test_create_customer_invalid_data(self, mock_query):
        data = {'name': ''} # Invalid data
        response = requests.post('http://localhost:5000/customers', json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

 # TestProductionEndpoints (test_production.py)
import unittest
from unittest.mock import patch
import requests

class TestProductionEndpoints(unittest.TestCase):

    @patch('app.models.Production.query')
    def test_get_production_success(self, mock_query):
        mock_query.get.return_value = {'id': 1, 'product_id': 1, 'quantity': 100}
        response = requests.get('http://localhost:5000/productions/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['quantity'], 100)

    @patch('app.models.Productions.query')
    def test_get_production_not_found(self, mock_query):
        mock_query.get.return_value # None
        response = requests.get('http://localhost:5000/productions/999')
        self.assertEqual(response.status_code, 404)

        @patch('app.models.Production.query')
        def test_create_production_invalid_data(self, mock_query):
            data = {'quantity': -10} # Invalid data
            response = requests.post('http://localhost:5000/productions', json=data)
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

# Task 4: Run and Validate Unit Tests
# Run all tests: 

# python -m unittest discover tests




    







