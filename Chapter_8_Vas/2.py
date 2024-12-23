class TExtNums:
    def __init__(self, input1: any, input2: any):
        if type(input1) == str and type(input2) == int:
            self.text = input1
            self.num = input2
        elif type(input1) == int and type(input2) == str:
            self.text = input1
            self.num = input2
        elif type(input1) == str and type(input2) == str:
            self.text = input1 + input2
            self.num = None
        elif type(input1) == int and type(input2) == int:
            self.num = input1 + input2
            self.text = None
        else:
            self.text = None
            self.num = None

    def show(self):
        for name in self.__dict__:
            if self.__dict__[name] != None:
                print(self.__dict__[name])
            else:
                print("No")


TExtNums.show(
    TExtNums('text', 'mama')
)
