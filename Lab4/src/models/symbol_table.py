from models.hash_table import HashTable


class SymbolTable:

    def __init__(self, size):
        self.table = HashTable(size)

    def add(self, new_entry):
        return self.table.add(new_entry)

    def get(self, key):
        return self.table.get(key)

    def contains(self, key):
        return self.table.contains(key)

    def remove(self, key):
        self.table.remove(key)

    def get_position(self, key):
        return self.table.get_position(key)

    def get_table(self):
        return self.table

    def __str__(self):
        return str(self.table)

    def print_symbol_table(self):
        for key in self.table.items():
            value = self.table.items()[key]
            print("{ ID:", value[0], ", Value:", value[1], "}")
