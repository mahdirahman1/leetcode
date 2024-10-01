class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.inc_array = [0] * maxSize
        self.top = -1

    def push(self, x: int) ->  None:
        if self.top < len(self.stack)-1:
            self.top += 1
            self.stack[self.top] = x
        

    def pop(self) -> int:
        if self.top == -1:
            return -1

        val = self.stack[self.top] + self.inc_array[self.top]
        self.top -= 1
        if self.top >= 0:
            self.inc_array[self.top] += self.inc_array[self.top+1]
        
        self.inc_array[self.top+1] = 0
        return val

    def increment(self, k: int, val: int) -> None:
        if self.top >= 0:
            index = min(k-1, self.top)
            self.inc_array[index] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)