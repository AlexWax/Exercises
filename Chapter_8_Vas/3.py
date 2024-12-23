class ListObj:
    def __init__(self, lst: list = None):
        self.newlist = []
        if type(lst) == list:
            self.lst = lst
        else:
            self.lst = None

        self.sort()

    def sort(self):
        if self.lst == None:
            self.show()
        else:
            [self.newlist.append(elem) for elem in self.lst if type(elem) == int]
            self.show(self.newlist)

    def show(self, name: list = None):
        if name != None:
            print(name)
            print(sum(name)/len(name))


A = ListObj([1, 2, 3, 'text', 4, 1.0, {1: 'a', 2: 'b'}])
