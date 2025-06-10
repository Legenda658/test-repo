import unittest
from src.feature_483 import calculate_feature_483, validate_feature_483
class TestFeature483(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_483(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_483(valid_data))
        self.assertFalse(validate_feature_483(invalid_data))
if __name__ == '__main__':
    unittest.main()