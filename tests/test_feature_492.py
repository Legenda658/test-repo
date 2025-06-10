import unittest
from src.feature_492 import calculate_feature_492, validate_feature_492
class TestFeature492(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_492(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_492(valid_data))
        self.assertFalse(validate_feature_492(invalid_data))
if __name__ == '__main__':
    unittest.main()