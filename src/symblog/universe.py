from typing import List

from .adjunct_class import AdjunctClass
from .thing import Thing


class Universe:
    """A universe is a collection of things.
    In principle, the universe is the collection of ALL things. However
    practically, it can be considered as a collection of things of a specific class.
    A Clases can be sampled from universes."""

    def __init__(self):
        self.things = []

    def add_thing(self, thing: Thing):
        self.things.append(thing)

    def add_things(self, things: List[Thing]):
        self.things.extend(things)

    def add_thing(self, thing: dict):
        self.things.append(Thing.from_attr(thing))

    def get_class(self, _class: AdjunctClass) -> List[Thing]:

        return [thing for thing in self.things if _class.is_member(thing)]

    def exists(self, _class: AdjunctClass) -> bool:
        return len(self.get_class(_class)) > 0

    def individual(self, _class: AdjunctClass) -> Thing:
        return len(self.get_class(_class)) == 1
