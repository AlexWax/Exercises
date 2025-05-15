import random


class TrainCounter:
    """
    Count number of wagons in train
    """
    def __init__(self):
        self.Flag = True
        self.counter = 0
        self.position = 0
        self.state = [True, random.choice([True, False])]
        """
        Start
        """
        self.loop()
        self.ans()

    def step(self, length: int = 1, step_mod: bool = True):
        """
        Change counter and current position
        :param length: Step length
        :param step_mod: If False, we not increase the counter
        """
        self.position += length
        self.counter += length * step_mod

    def switch(self):
        """
        Change state in wagon to False. Light off
        """
        train_length = random.randint(1, 10)
        self.state[self.counter != train_length] = False

    def loop(self):
        """
        Repeating steps, while Flag (Light in 0-wagon) is On
        """
        while self.Flag:
            self.step()
            self.switch()
            self.check()

    def check(self):
        """
        Check Flag state
        """
        if self.position:
            self.step(length=-self.counter, step_mod=False)
            self.check()
        else:
            self.Flag = self.state[0]
            self.step(length=self.counter, step_mod=False)

    def ans(self):
        """
        :return: desired train length
        """
        return self.counter
