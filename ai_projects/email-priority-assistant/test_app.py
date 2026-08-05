import unittest

from app import classify_email


class EmailClassifierTests(unittest.TestCase):
    def test_urgent_support_message(self):
        result = classify_email({"subject": "Urgent error", "body": "It failed today"})
        self.assertEqual(result.category, "support")
        self.assertEqual(result.priority, "high")

    def test_general_message(self):
        result = classify_email({"subject": "Hello", "body": "Thank you"})
        self.assertEqual(result.category, "general")
        self.assertEqual(result.priority, "normal")


if __name__ == "__main__":
    unittest.main()
