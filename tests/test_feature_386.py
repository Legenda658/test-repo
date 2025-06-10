import unittest
from src.feature_386 import calculate_feature_386, validate_feature_386
class TestFeature386(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_386(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_386(valid_data))
        self.assertFalse(validate_feature_386(invalid_data))
if __name__ == '__main__':
    unittest.main()