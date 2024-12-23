class BinarTree:
    def __init__(self, max_chain_length: int, iter: int = 0, direc: str = ''):

        self.__name__ = f"[{iter} {direc}]"
        self.next_left_nod_name = f"[{iter + 1} L]"
        self.next_right_nod_name = f"[{iter + 1} R]"
        self.max_chain_length = max_chain_length
        self.num_dif = 0

        if iter == max_chain_length:
            self.next_left_node = None
            self.next_right_node = None
            self.next_left_nod_name = None
            self.next_right_nod_name = None
        else:
            self.next_left_node = BinarTree(max_chain_length, iter + 1, direc='L')
            self.next_right_node = BinarTree(max_chain_length, iter + 1, direc='R')

    def show(self):
        print(self.__dict__)


def chain_obj(num: int, num_dis: int) -> object:
    return BinarTree(num, num_dis)


def show_chain_node(chain_object: object) -> object:
    a = chain_object
    if a != None:
        a.show()
        show_chain_node(a.next_left_node)
        show_chain_node(a.next_right_node)




Chain = BinarTree(2)

show_chain_node(Chain)

