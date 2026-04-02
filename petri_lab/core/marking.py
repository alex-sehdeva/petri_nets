from __future__ import annotations

from dataclasses import dataclass, field

from petri_lab.core.place import Place


@dataclass
class Marking:
    tokens: dict[str, int] = field(default_factory=dict)

    def get(self, place: Place) -> int:
        return self.tokens.get(place.name, 0)

    def add(self, place: Place, n: int = 1) -> None:
        if n < 0:
            raise ValueError("Cannot add a negative token count")
        self.tokens[place.name] = self.get(place) + n

    def remove(self, place: Place, n: int = 1) -> None:
        if n < 0:
            raise ValueError("Cannot remove a negative token count")
        if self.get(place) < n:
            raise ValueError(f"Not enough tokens in {place.name}")
        self.tokens[place.name] = self.get(place) - n

    def copy(self) -> "Marking":
        return Marking(self.tokens.copy())
