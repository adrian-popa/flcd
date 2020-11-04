class FiniteAutomata:

    def __init__(self, Q, sigma, q0, F, S):
        self.Q = Q
        self.sigma = sigma
        self.q0 = q0
        self.F = F
        self.S = S

    def get_Q(self):
        return 'Q = { ' + ', '.join(self.Q) + ' }'

    def get_sigma(self):
        return 'Σ = { ' + ', '.join(self.sigma) + ' }'

    def get_S(self):
        return 'S = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }'

    def get_F(self):
        return 'F = { ' + ', '.join(self.F) + ' }'

    def is_dfa(self):
        paths = {}
        for transition in self.S:
            state1, route = transition[0]
            if (state1, route) in paths.keys():
                paths[(state1, route)] += 1
            else:
                paths[(state1, route)] = 1
        for edge_count in paths.values():
            if edge_count > 1:
                return False
        return True


    @staticmethod
    def from_file(file_name):
        with open(file_name) as file:
            Q = FiniteAutomata.parse_line(file.readline())
            sigma = FiniteAutomata.parse_line(file.readline())
            q0 = file.readline().split('=')[1].strip()
            F = FiniteAutomata.parse_line(file.readline())
            S = FiniteAutomata.parse_transitions(FiniteAutomata.parse_line(''.join([line for line in file])))

            return FiniteAutomata(Q, sigma, q0, F, S)

    @staticmethod
    def parse_line(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    @staticmethod
    def parse_transitions(parts):
        result = []
        transitions = []
        index = 0

        while index < len(parts):
            transitions.append(parts[index] + ',' + parts[index + 1])
            index += 2

        for transition in transitions:
            lhs, rhs = transition.split('->')
            state2 = rhs.strip()
            state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]

            result.append(((state1, route), state2))

            # if (state1, route) in result:
            #     result[(state1, route)].append(state2)
            # else:
            #     result[(state1, route)] = [state2]

        return result

    def __str__(self):
        return 'The defined Finite Automata:\n' \
               + 'Q = { ' + ', '.join(self.Q) + ' }\n' \
               + 'Σ = { ' + ', '.join(self.sigma) + ' }\n' \
               + 'q0 = ' + str(self.q0) + '\n' \
               + 'F = { ' + ', '.join(self.F) + ' }\n' \
               + 'S = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n'
