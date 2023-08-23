import unittest
import pandas as pd
import json
from coupon import count_coupon_types, get_stats


class TestCouponFunctions(unittest.TestCase):

    with open('coupons.json', 'r') as json_file:
        json_data = json.load(json_file)

    # Convert the "coupons" data to a pandas DataFrame
    coupons_df = pd.DataFrame(json_data["coupons"])

    def test_count_coupon_types(self):
        # Test if count_coupon_types returns a dictionary
        result = count_coupon_types(self.coupons_df)
        self.assertIsInstance(result, dict)

    def test_get_stats(self):
        # Test if you get_stats returns a dictionary
        result = get_stats()
        self.assertIsInstance(result, dict)

        # Test if the expected keys exist in the result dictionary
        self.assertIn('promo_stats', result)
        self.assertIn('retailer', result)

        promo_stats = result['promo_stats']
        self.assertIn('coupon_type_counts', promo_stats)
        self.assertIn('discount_coupon_percentage', promo_stats)
        self.assertIn('dollar_discount', promo_stats)

        retailer_stats = result['retailer']
        self.assertIsInstance(retailer_stats, dict)


if __name__ == '__main__':
    unittest.main()
