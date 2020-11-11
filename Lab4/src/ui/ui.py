from models.finite_automata import FiniteAutomata


class UI:

    def __init__(self, finite_automata: FiniteAutomata):
        self.__finite_automata = finite_automata

    @staticmethod
    def print_menu():
        s = 'What would you like to display?\n'
        s += '1 - The set of states\n'
        s += '2 - The alphabet\n'
        s += '3 - All the transitions\n'
        s += '4 - The set of final states\n'
        s += '5 - Check valid DFA\n'
        s += '6 - Check accepted sequence\n'
        s += '0 - Exit'
        print(s)

    def run(self):
        self.print_menu()

        keep_alive = True
        while keep_alive:
            try:
                command = int(input('>> '))
                if command == 0:
                    keep_alive = False
                elif command == 1:
                    print(self.__finite_automata.get_Q())
                elif command == 2:
                    print(self.__finite_automata.get_sigma())
                elif command == 3:
                    print(self.__finite_automata.get_S())
                elif command == 4:
                    print(self.__finite_automata.get_F())
                elif command == 5:
                    if self.__finite_automata.is_dfa():
                        print("The Finite Automata is deterministic")
                    else:
                        print("The Finite Automata is nondeterministic")
                elif command == 6:
                    sequence = input('Give a sequence: ')
                    if self.__finite_automata.is_sequence_accepted(sequence):
                        print("Valid sequence")
                    else:
                        print("Invalid sequence")
                else:
                    print('Invalid command')
            except RuntimeError as e:
                print(e)
