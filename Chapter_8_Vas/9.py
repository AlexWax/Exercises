class ObjChain:
    def __init__(self, max_chain_length: int, iter: int = 0):

        self.__name__ = ObjChain.__name__ + f"[{iter}]"
        self.next_nod_name = ObjChain.__name__ + f"[{iter + 1}]"
        self.max_chain_length = max_chain_length
        self.num_dif = 0

        if iter == max_chain_length:
            self.next_nod = None
        else:
            self.next_nod = ObjChain(max_chain_length, iter+1)

    def show(self):
        print(self.__dict__)


def chain_obj(num: int, num_dis: int) -> object:
    return ObjChain(num, num_dis)


def show_chain_node(chain_object: object) -> object:
    a = chain_object
    print(Chain.max_chain_length)
    for i in range(Chain.max_chain_length):
        a.show()
        a = a.next_nod
    a.show()


def del_chain_node(chain_object: object, num_distr: int):
        a = chain_object
        a.max_chain_length -= 1
        a.num_dif -= 1
        for i in range(num_distr - 1):
            a = a.next_nod
        a.next_nod = ObjChain(a.max_chain_length - 1, num_distr+1)
        a.next_nod_name = ObjChain.__name__ + f"[{num_distr + 1}]"


def ins_chain_node(chain_object: object, num_ins: int):
    a = chain_object
    a.max_chain_length += 1
    a.num_dif += 1
    for i in range(num_ins - 1):
        a = a.next_nod
    a.next_nod = ObjChain(a.max_chain_length + 1, num_ins)
    a.next_nod_name = ObjChain.__name__ + f"[{num_ins}]"



Chain = ObjChain(10)

show_chain_node(Chain)
print('_____')
del_chain_node(Chain, 4)
print('_____')
show_chain_node(Chain)

