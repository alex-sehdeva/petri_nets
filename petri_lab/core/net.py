from dataclasses import dataclass

from petri_lab.core.place import Place
from petri_lab.core.transition import Transition


@dataclass(frozen=True)
class PetriNet:
    places: list[Place]
    transitions: list[Transition]
