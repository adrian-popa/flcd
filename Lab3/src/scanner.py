from constant import Constant
from hash_table import HashTable
from identifier import Identifier
from symbol_table import SymbolTable


class Scanner:

    def __init__(self, problem_file, tokens, separators):
        self.__problem_file = problem_file
        self.__tokens = tokens
        self.__separators = separators

        self.__pif = HashTable()
        self.__st = SymbolTable()

    def scan(self):
        line_count = 0
        for line in self.__problem_file.read().splitlines():
            line_count += 1
            for token in self.tokenize(line):
                if token in self.__tokens:
                    self.__pif.add(token, (-1, 1))
                elif isinstance(token, Identifier) or isinstance(token, Constant):
                    token_id = self.__st.add(token)
                    self.__pif.add(token, token_id)
                else:
                    print('Lexical error for token:', token, ', at line:', str(line_count))
                    return

    def tokenize(self, line):
        return line.split(str(self.__separators))

    def get_pif(self):
        return self.__pif

    def get_st(self):
        return self.__st
