import random


class TrainCounter:
    """
    Count number of wagons in train
    """
    def __init__(self):
        self._Flag = True
        self._counter = 0
        self._position = 0
        self._state = [True, random.choice([True, False])]

    def step(self, length: int = 1, step_mod: bool = True):
        """
        Change counter and current position
        :param length: Step length
        :param step_mod: If False, we not increase the counter
        """
        self._position += length
        self._counter += length * step_mod

    def switch(self):
        """
        Change state in wagon to False. Light off
        """
        train_length = random.randint(1, 10)
        self._state[self._counter != train_length] = False

    def loop(self):
        """
        Repeating steps, while _Flag (Light in 0-wagon) is On
        """
        while self._Flag:
            self.step()
            self.switch()
            self.check()

    def check(self):
        """
        Check _Flag state
        """
        if self._position:
            self.step(length=-self._counter, step_mod=False)
            self.check()
        else:
            self._Flag = self._state[0]
            self.step(length=self._counter, step_mod=False)

    def ans(self) -> int:
        """
        :return: desired train length
        """
        return self._counter


if __name__ == "__main__":
    count = TrainCounter()
    count.loop()
    print(count.ans())
