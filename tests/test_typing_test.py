import unittest
from utils.helpers import calculate_wpm, calculate_accuracy

class TestTypingTest(unittest.TestCase):
    def test_calculate_wpm(self):
        # Test cases for calculate_wpm function
        self.assertAlmostEqual(calculate_wpm(60, 60), 60)
        self.assertAlmostEqual(calculate_wpm(30, 30), 60)
        self.assertAlmostEqual(calculate_wpm(0, 60), 0)
        self.assertAlmostEqual(calculate_wpm(45, 90), 30)
        self.assertAlmostEqual(calculate_wpm(120, 60), 120)
        self.assertAlmostEqual(calculate_wpm(15, 0), 0)  # Handle division by zero

    def test_calculate_accuracy(self):
        # Test cases for calculate_accuracy function
        original = "The quick brown fox"
        typed_correct = "The quick brown fox"
        typed_incorrect = "The quik brown fx"
        correct, incorrect, total = calculate_accuracy(original, typed_correct)
        self.assertEqual(correct, 4)
        self.assertEqual(incorrect, 0)
        self.assertEqual(total, 4)

        correct, incorrect, total = calculate_accuracy(original, typed_incorrect)
        self.assertEqual(correct, 2)
        self.assertEqual(incorrect, 2)
        self.assertEqual(total, 4)

        # Test with extra words
        typed_extra = "The quick brown fox jumps over"
        correct, incorrect, total = calculate_accuracy(original, typed_extra)
        self.assertEqual(correct, 4)
        self.assertEqual(incorrect, 0)
        self.assertEqual(total, 4)

        # Test with missing words
        typed_missing = "The brown fox"
        correct, incorrect, total = calculate_accuracy(original, typed_missing)
        self.assertEqual(correct, 2)
        self.assertEqual(incorrect, 2)
        self.assertEqual(total, 4)

        # Test with completely wrong input
        typed_wrong = "Hello world this is wrong"
        correct, incorrect, total = calculate_accuracy(original, typed_wrong)
        self.assertEqual(correct, 0)
        self.assertEqual(incorrect, 4)
        self.assertEqual(total, 4)

        # Test with empty input
        typed_empty = ""
        correct, incorrect, total = calculate_accuracy(original, typed_empty)
        self.assertEqual(correct, 0)
        self.assertEqual(incorrect, 4)
        self.assertEqual(total, 4)

if __name__ == '__main__':
    unittest.main()
