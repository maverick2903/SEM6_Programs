class aggregate:
    def __init__(self):
        self.stack = []
        self.cost = 0
        self.totalOperations = 0

    def push(self, element):
        self.stack.append(element)
        self.cost += 1
        self.totalOperations += 1
        print(f"Pushed {element}")

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return
        popped = self.stack.pop()
        self.cost += 1
        self.totalOperations += 1
        print(f"Popped {popped}") 

    def multipop(self, k):
        print("Multipop starts")
        if not self.stack:
            print("Stack is empty")
            return
        while self.stack and k>0:
            k-=1
            self.pop()
        print("Multipop ends")

    def displayStack(self):
        print(self.stack,"\n")


stack = aggregate()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.multipop(2)

stack.pop()

print("Total Cost: ", stack.cost)
print("Total Operations: ", stack.totalOperations)
print("Amortized Cost per operation: ", stack.cost/stack.totalOperations)
