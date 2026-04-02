from petri_lab.core.engine import Engine
from petri_lab.core.marking import Marking
from petri_lab.core.net import PetriNet
from petri_lab.core.place import Place
from petri_lab.core.transition import Transition


def test_duplicate_send_is_structurally_prevented():
    idle = Place("Idle")
    signal = Place("Signal")
    ready = Place("ReadyToSend")
    sent = Place("OrderSent")

    net = PetriNet(
        places=[idle, signal, ready, sent],
        transitions=[
            Transition("receive_signal", {idle: 1}, {signal: 1}),
            Transition("validate_signal", {signal: 1}, {ready: 1}),
            Transition("send_order", {ready: 1}, {sent: 1}),
        ],
    )

    engine = Engine(net=net, marking=Marking({"Idle": 1}))

    engine.step("receive_signal")
    engine.step("validate_signal")
    engine.step("send_order")

    assert engine.marking.tokens["OrderSent"] == 1
    assert "send_order" not in [t.name for t in engine.enabled_transitions()]
