from models.constant import Constant
from models.identifier import Identifier
from models.program_internal_form import ProgramInternalForm
from models.symbol_table import SymbolTable


class Scanner:

    def __init__(self, problem_file, reserved_words, separators, operators):
        self.__problem_file = problem_file
        self.__reserved_words = reserved_words
        self.__separators = separators
        self.__operators = operators

        self.__st = SymbolTable(21)
        self.__pif = ProgramInternalForm()

        self.__lexicalError = False

    def scan(self):
        line_count = 0
        lexical_error = None
        for line in self.__problem_file.read().splitlines():
            line_count += 1
            for token in self.tokenize(line):
                if token in self.__reserved_words or token in self.__separators or token in self.__operators:
                    if token == ' ':
                        continue
                    self.__pif.add(token, (-1, 1))
                elif isinstance(token, Identifier) or isinstance(token, Constant):
                    token_id = self.__st.add(token)
                    self.__pif.add(token, token_id)
                else:
                    if lexical_error is None:
                        lexical_error = 'Lexical error for token: ' + token + ', at line: ' + str(line_count)
        print(lexical_error)

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_operator_token(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.get_operator_token(line, index)
                tokens.append(token)
                token = ''
            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.get_string_token(line, index)
                tokens.append(token)
                token = ''
            elif line[index] in self.__separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''
            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def is_operator_token(self, char):
        for operator in self.__operators:
            if char in operator:
                return True
        return False

    def get_operator_token(self, line, index):
        token = ''
        while index < len(line) and self.is_operator_token(line[index]):
            token += line[index]
            index += 1
        return token, index

    @staticmethod
    def get_string_token(line, index):
        token = ''
        no_of_quotes = 0
        while index < len(line) and no_of_quotes < 2:
            if line[index] == '\'':
                no_of_quotes += 1
            token += line[index]
            index += 1
        return token, index

    def get_pif(self):
        return self.__pif

    def get_st(self):
        return self.__st
