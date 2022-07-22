from typing import List, Dict

from ..adl import Action
from .adjunct_class import AdjunctClass
from .thing import Thing


class Universe:
    """A universe is a collection of things.
    In principle, the universe is the collection of ALL things. However
    practically, it can be considered as a collection of things of a specific class.
    A Clases can be sampled from universes."""

    @classmethod
    def from_things(cls, things: List[Thing]) -> "Universe":
        universe = cls()
        universe.add_things(things)
        return universe

    @classmethod
    def from_attrs(cls, attrs: List[dict]) -> "Universe":
        universe = cls()
        universe.add_things([Thing.from_attr(attr) for attr in attrs])
        return universe

    @classmethod
    def generate_from_class(cls, _class: AdjunctClass, n: int) -> "Universe":
        return cls.from_things(_class.create_n(n))

    def __init__(self):
        self.things = []

    def add_thing(self, thing: Thing):
        self.things.append(thing)

    def add_things(self, things: List[Thing]):
        self.things.extend(things)

    def add_thing(self, thing: dict):
        self.things.append(Thing.from_attr(thing))

    def __len__(self):
        return len(self.things)

    def get_class(self, _class: AdjunctClass) -> List[Thing]:

        return [thing for thing in self.things if _class.is_member(thing)]

    def exists(self, _class: AdjunctClass) -> bool:
        return len(self.get_class(_class)) > 0

    def individual(self, _class: AdjunctClass) -> Thing:
        return len(self.get_class(_class)) == 1

    def do(self, action: Action, n: int = 1):

        precondition_things = self.get_action_operands(action)

        for name, things in precondition_things.items():
            if len(things) < n:
                raise Exception(
                    f"Not enough preconditions for {n} executions of action: {name}: {len(things)}"
                )
        out_ops = []
        for i in range(n):
            ops = {op: things[i] for op, things in precondition_things.items()}
            action.execute(ops)
            out_ops.append(ops)

        return out_ops

    def get_action_operands(self, action: Action) -> Dict[str, List[Thing]]:
        # NOTE: (ZD) this will return the operands in the order which they are found.
        return {op: self.get_class(c) for op, c in action.preconditions.items()}
