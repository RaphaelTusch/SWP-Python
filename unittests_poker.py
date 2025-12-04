import unittest
from Poker2 import detectCombination

class TestPoker(unittest.TestCase):

    def test_royal_flush(self):
        hand = [8, 9, 10, 11, 12]   # Pik 10, J, Q, K, A
        self.assertEqual(detectCombination(hand), "Royal Flush")

    def test_full_house(self):
        hand = [4, 17, 30, 7, 20]   # 4,4,4 / 7,7
        self.assertEqual(detectCombination(hand), "Full House")

    def test_straight(self):
        hand = [1, 14, 27, 5, 18]   # 2–3–4–5–6 Straße
        self.assertEqual(detectCombination(hand), "Straight")

    def test_two_pair(self):
        hand = [9, 22, 12, 25, 38]  # 9,9 + 12,12
        self.assertEqual(detectCombination(hand), "Two Pair")


if __name__ == "__main__":
    unittest.main()
