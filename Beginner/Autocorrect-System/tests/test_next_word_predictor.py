import unittest
from src.next_word_predictor import NextWordPredictor


class TestNextWordPredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = NextWordPredictor()

    def test_known_bigram(self):
        predictions = self.predictor.predict_next_word("i love")
        self.assertIn("machine", predictions)
        self.assertIn("python", predictions)

    def test_empty_input(self):
        self.assertEqual(self.predictor.predict_next_word(""), [])

    def test_prediction_limit(self):
        predictions = self.predictor.predict_next_word("i", limit=2)
        self.assertLessEqual(len(predictions), 2)

    def test_unknown_context_fallback(self):
        predictions = self.predictor.predict_next_word("unseenword")
        self.assertTrue(len(predictions) > 0)


if __name__ == "__main__":
    unittest.main()