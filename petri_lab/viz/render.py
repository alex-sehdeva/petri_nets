from petri_lab.core.engine import Engine
from petri_lab.core.marking import Marking


def format_marking(marking: Marking) -> str:
    if not marking.tokens:
        return "Current marking: <empty>"
    lines = ["Current marking:"]
    for place in sorted(marking.tokens):
        lines.append(f"  - {place}: {marking.tokens[place]}")
    return "\n".join(lines)


def format_enabled(engine: Engine) -> str:
    enabled = [t.name for t in engine.enabled_transitions()]
    return f"Enabled transitions: {enabled}"
