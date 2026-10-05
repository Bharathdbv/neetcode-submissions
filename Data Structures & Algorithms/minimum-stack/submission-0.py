class MinStack:

    def __init__(self):
        self.stack = []
        self.minel = 2**31 - 1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minel = min(self.minel,val)

    def pop(self) -> None:
        if self.stack :
            k = self.stack[len(self.stack) - 1]
            del self.stack[len(self.stack) - 1]
            return k

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return min(self.stack)
