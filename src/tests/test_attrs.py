import random
import unittest

from .. import attrs


class TestRandomEnum(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(0)

    def test_random_enum(self):
        self.assertEqual(attrs.FaceValues.get_random(), attrs.FaceValues.KING)
        self.assertEqual(attrs.Suits.get_random(), attrs.Suits.WANDS)


if __name__ == "__main__":
    unittest.main()
