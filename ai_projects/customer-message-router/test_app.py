import unittest

from app import route_message


class MessageRouterTests(unittest.TestCase):
    def test_sales_route(self):
        result = route_message({"customer": "Test", "message": "Please send a price quote"})
        self.assertEqual(result.route, "sales")
        self.assertTrue(result.requires_human_review)

    def test_urgent_support_route(self):
        result = route_message({"customer": "Test", "message": "Urgent login error today"})
        self.assertEqual(result.route, "technical_support")
        self.assertEqual(result.priority, "high")


if __name__ == "__main__":
    unittest.main()
