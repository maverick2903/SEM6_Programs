class potential:
    def __init__(self):
        self.stack = []
        self.cost = 0
        self.totalOperations = 0
        self.amortizedCost = 0

    def push(self, element):
        self.stack.append(element)
        self.cost += 1
        self.totalOperations += 1
        self.amortizedCost += 1 + len(self.stack) - (len(self.stack)-1)
        print(f"Pushed {element}")
        print("Stack: ",self.stack)
        print(f"Amortized Cost = actual cost(1) + state of stack after operation ({len(self.stack)}) - state of stack before operation ({len(self.stack)-1})\n")
        

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return
        popped = self.stack.pop()
        self.cost += 1
        self.totalOperations += 1
        self.amortizedCost += 1 + len(self.stack) - (len(self.stack)+1)
        print(f"Popped {popped}") 
        print("Stack: ",self.stack)
        print(f"Amortized Cost = actual cost(1) + state of stack after operation ({len(self.stack)}) - state of stack before operation ({len(self.stack)+1})\n")


    def multipop(self, k):
        temp = k
        print("Multipop starts")
        if not self.stack:
            print("Stack is empty")
            return
        while self.stack and k>0:
            k-=1
            self.stack.pop()
            self.cost+=1
            self.totalOperations+=1
        print("Multipop ends")
        print("Stack: ",self.stack)
        self.amortizedCost+= temp+ len(self.stack) - (len(self.stack)+temp)
        print("Stack after multipop: ",self.stack)



stack = potential()

stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()

stack.multipop(2)



print("Total Cost: ", stack.cost)
print("Total Operations: ", stack.totalOperations)
print("Amortized Cost: ", stack.amortizedCost)
