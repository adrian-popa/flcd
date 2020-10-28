class ProgramInternalForm:

    def __init__(self):
        self.__list = []

    def add(self, token, position):
        self.__list.append((token, position))

    def __str__(self):
        result = 'Program Internal Form\n'
        for pair in self.__list:
            result += pair[0] + ' -> ' + str(pair[1]) + '\n'
        return result
