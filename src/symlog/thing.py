from numbers import Number
from typing import List


class Thing:
    """A thing is an object that has attributes.
    Things typically represent extant objects in the world."""

    def __init__(self):
        self.attr = {}

    @classmethod
    def from_attr(cls, attr):
        thing = cls()
        thing.attr = attr
        return thing

    def has(self, attr: str) -> bool:
        return attr in self.attr

    def get(self, attr: str) -> object:
        if not self.has(attr):
            raise ValueError(f"{self} does not have {attr}")
        return self.attr[attr]

    def __eq__(self, __o: object) -> bool:

        if isinstance(__o, Thing):
            return self.attr == __o.attr
        elif isinstance(__o, dict):
            return self.attr == __o
        else:
            return False

    def contains(self, attr: str, thing: "Thing") -> bool:

        if not self.has(attr):
            raise ValueError(f"{self} does not have {attr}")

        attr = self.attr[attr]
        if not isinstance(attr, list):
            raise ValueError(f"{attr} is not a collection")

        return thing in attr

    def incr(self, attr: str, amount: int = 1) -> None:
        if not self.has(attr):
            raise ValueError(f"{self} does not have {attr}")
        if not isinstance(self.attr[attr], Number):
            raise ValueError(f"{self}'s {attr} is not a number")

        self.attr[attr] += amount
