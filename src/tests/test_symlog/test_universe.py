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

    def test_get_class(self):
        self.assertEqual(len(self.u.get_class(AdjunctClass("all"))), 2)
        self.assertEqual(len(self.u.get_class(self.c1)), 1)
        self.assertEqual(len(self.u.get_class(self.c2)), 1)

    def test_exists(self):
        self.assertTrue(self.u.exists(AdjunctClass("all")))
        self.assertTrue(self.u.exists(self.c1))
        self.assertTrue(self.u.exists(self.c2))

        self.assertFalse(self.u.exists(AdjunctClass("c3", {"c": lambda: 0})))
