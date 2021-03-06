class Constant:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.get_key()

    def __str__(self):
        return self.key + " " + str(self.value)

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value
