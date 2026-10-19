
import unittest
from src.autocorrect import AutocorrectSystem


class TestAutocorrectSystem(unittest.TestCase):
    def setUp(self):
        self.autocorrect = AutocorrectSystem()

    def test_correct_word(self):
        self.assertEqual(
            self.autocorrect.correct_word("speling"),
            "spelling"
        )

    def test_correct_sentence(self):
        result = self.autocorrect.correct_text("I hav a beutiful cat")
        self.assertIn("have", result)
        self.assertIn("beautiful", result)

    def test_empty_text(self):
        self.assertEqual(self.autocorrect.correct_text(""), "")

    def test_punctuation(self):
        result = self.autocorrect.correct_word("speling!")
        self.assertEqual(result, "spelling!")

    def test_suggestions(self):
        suggestions = self.autocorrect.suggest_corrections("speling")
        self.assertIn("spelling", suggestions)


if __name__ == "__main__":
    unittest.main()
