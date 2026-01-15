class Queue:
    def __init__(self):
        # Vytvoř prázdný seznam pro uložení prvků
        self.data = []
        pass
    
    def enqueue(self, prvek):
        # Přidá prvek na konec fronty
        self.data.append(prvek)
        
    
    def dequeue(self):
        # Odebere prvek ze začátku fronty
        # Nezapomeň zkontrolovat, jestli není prázdná!
        if self.isEmpty():
            return None
        return self.data.pop(0)
        
    
    def peek(self):
        # Podívá se na začátek, ale neodebere
        if self.isEmpty():
            return None
        return self.data[0]
        
    
    def isEmpty(self):
        # Vrátí True pokud je prázdná, jinak False
        return len(self.data) == 0
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # 1
print(q.dequeue())  # 2
print(q.peek())     # 3
print(q.dequeue())  # 3
print(q.isEmpty())  # True
print(q.dequeue())