from Tonk import Deck, Tonk
import unittest

class BinarizedDecisionTree_Test(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.tonk = Tonk()

    def test_choose_discard(self):
        self.assertEqual(self.tonk.choose_discard([1,1,1,2]), 1)
        self.assertEqual(self.tonk.choose_discard([10,13,13]), 13)
        self.assertEqual(self.tonk.choose_discard([9,9,9,13,13]), 9)
        self.assertEqual(self.tonk.choose_discard([1,2,3,4,5]), 5)


if __name__ == '__main__':
    unittest.main()
