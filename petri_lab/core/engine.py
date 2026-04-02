from __future__ import annotations

from dataclasses import dataclass

from petri_lab.core.marking import Marking
from petri_lab.core.net import PetriNet
from petri_lab.core.transition import Transition


@dataclass
class Engine:
    net: PetriNet
    marking: Marking

    def enabled_transitions(self) -> list[Transition]:
        return [t for t in self.net.transitions if t.is_enabled(self.marking)]

    def step(self, transition_name: str | None = None) -> Transition | None:
        enabled = self.enabled_transitions()
        if not enabled:
            return None

        if transition_name is None:
            transition = enabled[0]
        else:
            transition = next((t for t in enabled if t.name == transition_name), None)
            if transition is None:
                raise ValueError(f"Transition {transition_name} is not currently enabled")

        self.marking = transition.fire(self.marking)
        return transition

    def run(self, steps: int = 10) -> list[str]:
        fired: list[str] = []
        for _ in range(steps):
            transition = self.step()
            if transition is None:
                break
            fired.append(transition.name)
        return fired
