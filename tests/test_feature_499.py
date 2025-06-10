import unittest
from src.feature_499 import calculate_feature_499, validate_feature_499
class TestFeature499(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_499(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_499(valid_data))
        self.assertFalse(validate_feature_499(invalid_data))
if __name__ == '__main__':
    unittest.main()