import unittest

from app import organize_intake


class IntakeOrganizerTests(unittest.TestCase):
    def test_missing_documents(self):
        result = organize_intake({"reference": "X", "matter_type": "property_sale", "received_documents": []})
        self.assertEqual(result.status, "awaiting_documents")
        self.assertEqual(len(result.missing_documents), 4)

    def test_complete_intake(self):
        documents = ["Identity document", "Business name", "Registered address", "Ownership details"]
        result = organize_intake({"matter_type": "business_setup", "received_documents": documents})
        self.assertEqual(result.status, "ready_for_review")


if __name__ == "__main__":
    unittest.main()
