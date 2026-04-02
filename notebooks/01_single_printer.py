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
    printer_free = Place("PrinterFree")
    job_waiting = Place("JobWaiting")
    printing = Place("Printing")
    done = Place("Done")

    start_print = Transition(
        "start_print",
        inputs={printer_free: 1, job_waiting: 1},
        outputs={printing: 1},
    )
    finish_print = Transition(
        "finish_print",
        inputs={printing: 1},
        outputs={printer_free: 1, done: 1},
    )

    net = PetriNet(
        places=[printer_free, job_waiting, printing, done],
        transitions=[start_print, finish_print],
    )

    initial = Marking({printer_free.name: 1, job_waiting.name: 2})
    return initial, net


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
def _(initial, reset, state, step):
    engine = state()
    if reset.value:
        engine.marking = initial.copy()
    if step.value:
        engine.step()
    state(engine)
    return engine


@app.cell
def _(engine):
    marimo.md("## Single Printer Petri Net")
    marimo.md("Only one print job can be active because `PrinterFree` has capacity 1.")
    marimo.md(f"```\n{format_marking(engine.marking)}\n```")
    marimo.md(format_enabled(engine))


@app.cell
def _(reset, step):
    marimo.hstack([step, reset])


if __name__ == "__main__":
    app.run()
