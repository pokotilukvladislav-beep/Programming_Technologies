import unittest
from fastapi.testclient import TestClient
from auction_service import app, auction_items, bids_history


class AuctionServiceTests(unittest.TestCase):

    def setUp(self):
        auction_items.clear()
        bids_history.clear()
        self.client = TestClient(app)

    def test_create_item_success(self):
        response = self.client.post(
            "/items/",
            json={"item_id": "lot1", "name": "Antique Watch", "start_price": 100.0}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "item_created")

    def test_create_duplicate_item_fails(self):
        payload = {"item_id": "lot1", "name": "Antique Watch", "start_price": 100.0}
        self.client.post("/items/", json=payload)
        response = self.client.post("/items/", json=payload)
        self.assertEqual(response.status_code, 400)

    def test_place_bid_item_not_found(self):
        response = self.client.post(
            "/bids/",
            json={"item_id": "unknown_lot", "bid_amount": 150.0}
        )
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
