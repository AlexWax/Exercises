class ChainClass:
    def __init__(self, num):
        self.number = num
        # print(f"Create {self.number} elem of chain")

        if num > 0:
            self.next = ChainClass(num-1)

        self.__name__ = ChainClass.__name__ + str(num)

    def __del__(self):
        pass
        # print(f'Del {self.number} elem of chain')

    def show(self):
        print(self.__name__)





def chain_obj(num: int) -> object:
    return ChainClass(num)


print(chain_obj(2).__dict__)