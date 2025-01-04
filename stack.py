class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.stack=[]
        pass
    # You can implement this class however you like
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
    def top(self):
        if len(self.stack)>0:
            return self.stack[-1]
    def len(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack)==0
    def prt(self):
        return self.stack