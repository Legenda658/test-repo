import unittest
from src.feature_449 import calculate_feature_449, validate_feature_449
class TestFeature449(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_449(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_449(valid_data))
        self.assertFalse(validate_feature_449(invalid_data))
if __name__ == '__main__':
    unittest.main()