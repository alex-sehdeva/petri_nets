from petri_lab.core.engine import Engine
from petri_lab.core.marking import Marking
from petri_lab.core.net import PetriNet
from petri_lab.core.place import Place
from petri_lab.core.transition import Transition


def test_traffic_light_cycles():
    red = Place("Red")
    green = Place("Green")
    yellow = Place("Yellow")

    net = PetriNet(
        places=[red, green, yellow],
        transitions=[
            Transition("to_green", {red: 1}, {green: 1}),
            Transition("to_yellow", {green: 1}, {yellow: 1}),
            Transition("to_red", {yellow: 1}, {red: 1}),
        ],
    )

    engine = Engine(net=net, marking=Marking({"Red": 1}))
    fired = engine.run(steps=3)

    assert fired == ["to_green", "to_yellow", "to_red"]
    assert engine.marking.tokens == {"Red": 1, "Green": 0, "Yellow": 0}


def test_invalid_transition_name_raises():
    idle = Place("Idle")
    done = Place("Done")

    net = PetriNet(
        places=[idle, done],
        transitions=[Transition("finish", {idle: 1}, {done: 1})],
    )

    engine = Engine(net=net, marking=Marking({"Idle": 1}))

    try:
        engine.step("missing")
    except ValueError as exc:
        assert "not currently enabled" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unknown transition")
