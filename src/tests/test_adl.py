import unittest

from .. import adl
from .. import symlog


class TestActionDo(unittest.TestCase):
    def setUp(self) -> None:

        self.c = symlog.AdjunctClass("class", {"b": lambda: 0})

        self.action = adl.Action("action", {"a": self.c}, {"a": lambda x: x.incr("b")})

    def test_action_do(self):

        self.things = {"a": self.c.create()}

        self.action.do(self.things)

        self.assertEqual(self.things["a"].get("b"), 1)
