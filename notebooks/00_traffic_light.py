import marimo

from petri_lab.core.engine import Engine
from petri_lab.core.marking import Marking
from petri_lab.core.net import PetriNet
from petri_lab.core.place import Place
from petri_lab.core.transition import Transition
from petri_lab.viz.render import format_enabled, format_marking

app = marimo.App(width="medium")


@app.cell
def _():
    red = Place("Red")
    green = Place("Green")
    yellow = Place("Yellow")

    to_green = Transition("to_green", inputs={red: 1}, outputs={green: 1})
    to_yellow = Transition("to_yellow", inputs={green: 1}, outputs={yellow: 1})
    to_red = Transition("to_red", inputs={yellow: 1}, outputs={red: 1})

    net = PetriNet(
        places=[red, green, yellow],
        transitions=[to_green, to_yellow, to_red],
    )
    initial = Marking({red.name: 1})
    return initial, net, red


@app.cell
def _(initial, net):
    state = marimo.state(Engine(net=net, marking=initial.copy()))
    return state


@app.cell
def _(state):
    reset = marimo.ui.button(label="Reset")
    step = marimo.ui.button(label="Step")
    return reset, step


@app.cell
def _(initial, red, reset, state, step):
    engine = state()
    if reset.value:
        engine.marking = Marking({red.name: 1})
    if step.value:
        engine.step()
    state(engine)
    return engine


@app.cell
def _(engine):
    marimo.md("## Traffic Light Petri Net")
    marimo.md(f"```\n{format_marking(engine.marking)}\n```")
    marimo.md(format_enabled(engine))


@app.cell
def _(reset, step):
    marimo.hstack([step, reset])


if __name__ == "__main__":
    app.run()
