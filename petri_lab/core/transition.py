from __future__ import annotations

from dataclasses import dataclass

from petri_lab.core.marking import Marking
from petri_lab.core.place import Place


@dataclass(frozen=True)
class Transition:
    name: str
    inputs: dict[Place, int]
    outputs: dict[Place, int]

    def is_enabled(self, marking: Marking) -> bool:
        return all(marking.get(place) >= count for place, count in self.inputs.items())

    def fire(self, marking: Marking) -> Marking:
        if not self.is_enabled(marking):
            raise ValueError(f"Transition {self.name} is not enabled")

        new_marking = marking.copy()
        for place, count in self.inputs.items():
            new_marking.remove(place, count)
        for place, count in self.outputs.items():
            new_marking.add(place, count)
        return new_marking
