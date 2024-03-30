

import unittest
from flask import json
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        # Define sample input data
        input_data = {
            'sepal_length': 5.1,
            'sepal_width': 3.5,
            'petal_length': 1.4,
            'petal_width': 0.2,
            'PetalLengthCm':0.3
        }

        # Send POST request to /predict endpoint
        response = self.app.post('/predict', json=input_data)
        
        # Verify response status code
        self.assertEqual(response.status_code, 200, msg=f"Response: {response.data}")

        # Parse JSON response
        response_data = json.loads(response.data)
        
        # Verify response contains 'prediction' key
        self.assertIn('prediction', response_data)

        # Verify prediction value is of type int
        self.assertIsInstance(response_data['prediction'], str)

    def tearDown(self):
        # Clean up any resources or objects used in the tests
        pass

if __name__ == '__main__':
    unittest.main()
