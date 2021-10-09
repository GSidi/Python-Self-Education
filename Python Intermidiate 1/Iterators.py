#remote controll class

class RemoteControl():
    def __init__(self):
        self.channels = ["star", "ant1", "mega", "alpha", "ert1"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

