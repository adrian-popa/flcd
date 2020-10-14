from hash_table import HashTable
from symbol_table import SymbolTable


def main():
    hash_table = HashTable(10)

    identifiers_st = SymbolTable(hash_table)
    constants_st = SymbolTable(hash_table)

    hash_table.add('a', 5)
    hash_table.add('b', 7)
    hash_table.add('c', 12)
    hash_table.add('b', 'c')


main()
