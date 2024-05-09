class accounting:
    def __init__(self):
        self.stack = []
        self.cost = 0
        self.totalOperations = 0
        self.amortizedCost = 0
        self.creditBank = 0

    def push(self, element):
        self.stack.append(element)
        self.cost += 1
        self.totalOperations += 1
        self.amortizedCost += 2
        self.creditBank += 1
        print(f"Pushed {element}")
        self.displayStack()
        

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return
        popped = self.stack.pop()
        self.cost += 1
        self.totalOperations += 1
        self.amortizedCost += 1
        self.creditBank -= 1
        print(f"Popped {popped}") 
        self.displayStack()


    def multipop(self, k):
        print("Multipop starts")
        if not self.stack:
            print("Stack is empty")
            return
        while self.stack and k>0:
            k-=1
            self.pop()
        print("Multipop ends")
        self.displayStack()


    def displayStack(self):
        print(self.stack)
        print(f"Credit Bank: {self.creditBank}\n")


stack = accounting()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.multipop(2)

stack.pop()

print("Total Cost: ", stack.cost)
print("Total Operations: ", stack.totalOperations)
print("Amortized Cost: ", stack.amortizedCost)
