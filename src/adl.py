from typing import Callable, Dict

from .symlog import Thing, AdjunctClass


class Action:
    """Action represents a possible action in the world.
    Actions have"""

    def __init__(
        self, name, preconditions: Dict[str, AdjunctClass], effect=Dict[str, Callable]
    ):

        self.name = name
        self.preconditions = preconditions
        self.effect = effect

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} action"

    def __eq__(self, other):

        if isinstance(other, Action):
            return (
                self.preconditions == other.preconditions
                and self.effect == other.effect
            )

        return False

    def do(self, things: Dict[str, Thing]):
        for op, e in self.effect.items():
            thing = things[op]
            e(thing)
