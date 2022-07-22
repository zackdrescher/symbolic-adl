import unittest

from ...adl import Action
from ...symlog import Universe, AdjunctClass


class TestUniverse(unittest.TestCase):
    def setUp(self) -> None:

        self.c1 = AdjunctClass("c1", {"a": lambda: 0})
        self.c2 = AdjunctClass("c2", {"b": lambda: 0})

        self.u = Universe.from_things([self.c1.create(), self.c2.create()])

    def test_len(self):
        self.assertEqual(len(self.u), 2)
