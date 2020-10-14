class SymbolTable:

    def __init__(self, hash_table):
        self.__st = {}
        self.__hash_table = hash_table

    def add(self, position, identifier):
        self.__st[position] = identifier
