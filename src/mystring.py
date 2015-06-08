class MyString:
    def __init__(self, value):
        self.value = value

    def reverse(self):
        newst = ''
        length = len(self.value) - 1
        while length > - 1:
            newst = newst + self.value[length]
            length = length - 1
        return newst
