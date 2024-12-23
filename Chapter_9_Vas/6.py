class Fb:
    def __init__(self, lst: list):
        self.lst_giv = lst
        self.new_lst_out = self.check()

    def __getattribute__(self, item):
        if item == 'new_lst_out':
            text_out = ''
            for elem in object.__getattribute__(self, item):
                text_out += elem[:1].upper() + '\n'
            return text_out
        else:
            return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print('Nothing!')

    def check(self):
        if type(self.lst_giv) == list:
            lst = self.lst_giv
        else:
            lst = []

        new_lst = []
        [new_lst.append(elem) for elem in lst if type(elem) == str]
        return new_lst


A = Fb([1, '2', 3, 'abc', 'vyaxaxaa'])
print(A.new_lst_out)