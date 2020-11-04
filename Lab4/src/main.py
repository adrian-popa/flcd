from models.finite_automata import FiniteAutomata
from ui.ui import UI


def main():
    finite_automata = FiniteAutomata.from_file('FA.in')
    print(finite_automata)
    ui = UI(finite_automata)
    ui.run()


main()
