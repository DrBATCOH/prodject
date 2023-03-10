class Alphabet:
    def __init__(self, end_: str, lower_=True):
        self.start = ord("a")
        self.end_ = end_
        self.lower_ = lower_

        if self.lower_ is False:
            self.start = ord("A")
            self.end_ = self.end_.upper()

    def __next__(self):
        if self.value == ord(self.end_):
            raise StopIteration

        else:
            self.value += 1

        return chr(self.value)

    def __iter__(self):
        self.value = self.start - 1
        return self


for letter in Alphabet(end_="r", lower_=False):
    print(letter)
