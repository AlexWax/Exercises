class SubStrings:
    def __init__(self, lst: list):
        self.subs_lst_out = [set(lst)]
        self.subs(lst)

    def subs(self, lst):
        if len(lst) == 1:
            return self.subs_lst_out
        subs_lst = []
        for i in range(len(lst)):
            cur_set = []
            [cur_set.append(elem) for elem in lst[:i]+lst[i+1:] if elem not in cur_set]
            subs_lst.append(cur_set)
        [self.subs_lst_out.append(set(elem)) for elem in subs_lst if set(elem) not in self.subs_lst_out]
        for elem in subs_lst:
            self.subs(elem)


print(SubStrings([1, 2, 3, 1, 15]).subs_lst_out)
