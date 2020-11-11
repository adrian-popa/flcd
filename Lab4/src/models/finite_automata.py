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
        return 'S = { ' + ', '.join([(str(key) + ' -> ' + str(self.S[key])) for key in self.S.keys()]) + ' }'

    def get_F(self):
        return 'F = { ' + ', '.join(self.F) + ' }'

    def is_dfa(self):
        for transition in self.S.keys():
            if len(self.S[transition]) > 1:
                return False
        return True

    def is_sequence_accepted(self, sequence):
        if not self.is_dfa():
            return False
        state = self.q0
        for symbol in sequence.strip():
            if (state, symbol) not in self.S.keys():
                return False
            state = self.S[state, symbol][0]
        return state in self.F

    @staticmethod
    def from_file(file_name):
        with open(file_name) as file:
            Q = FiniteAutomata.parse_line(file.readline())
            sigma = FiniteAutomata.parse_line(file.readline())
            q0 = file.readline().split('=')[1].strip()
            F = FiniteAutomata.parse_line(file.readline())
            S = FiniteAutomata.parse_transitions(FiniteAutomata.parse_line(''.join([line for line in file])))

            if not FiniteAutomata.is_valid(Q, sigma, q0, F, S):
                print("Invalid FA read from file.")
                return None

            return FiniteAutomata(Q, sigma, q0, F, S)

    @staticmethod
    def parse_line(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    @staticmethod
    def parse_transitions(parts):
        result = {}
        transitions = []
        index = 0

        while index < len(parts):
            transitions.append(parts[index] + ',' + parts[index + 1])
            index += 2

        for transition in transitions:
            lhs, rhs = transition.split('->')
            state2 = rhs.strip()
            state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]

            if (state1, route) in result:
                result[(state1, route)].append(state2)
            else:
                result[(state1, route)] = [state2]

        return result

    @staticmethod
    def is_valid(Q, sigma, q0, F, S):
        if q0 not in Q:
            return False
        for transition in S.keys():
            state1, route = transition
            if state1 not in Q:
                return False
            if route not in sigma:
                return False
            for state2 in S[transition]:
                if state2 not in Q:
                    return False
        for state2 in F:
            if state2 not in Q:
                return False
        return True

    def __str__(self):
        return 'The defined Finite Automata:\n' \
               + 'Q = { ' + ', '.join(self.Q) + ' }\n' \
               + 'Σ = { ' + ', '.join(self.sigma) + ' }\n' \
               + 'q0 = ' + str(self.q0) + '\n' \
               + 'F = { ' + ', '.join(self.F) + ' }\n' \
               + 'S = { ' + ', '.join([(str(key) + ' -> ' + str(self.S[key])) for key in self.S.keys()]) + ' }\n'
