
class Chain:
    """Chain creation"""
    def __init__(self, name: str, num: int = 1):
        self.name = name
        """Main block"""
        if num == 1:
            self.next = None    # Stop
        else:
            self.next = Chain(self.name, num-1)     # Go further
        """__________"""
        self.set()

    def __del__(self):
        print(self.code)

    def set(self, num: int = 1):
        """Create text to output"""
        self.code = self.name + f'[{str(num)}]'
        if self.next != None:
            self.next.set(num+1)

    def show(self):
        """Output chain"""
        print(self.code)
        if self.next != None:
            self.next.show()



A = Chain('Alpha', 1)
A.show()
print(Chain.__dict__)
print(A.__dict__)




