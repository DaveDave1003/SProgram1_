class Stack:
    def __init__(self):
        self.list = []
        pass
    
    def push(self, prvek):
        # Přidá prvek na vrchol zásobníku
        self.list.append(prvek)
        

    def isEmpty(self):
        # Vrátí True pokud je prázdný, jinak False
        return len(self.list) == 0
        
   
    def pop(self):
        if(self.isEmpty()):
            return None
        
        # Odebere a vrátí prvek z vrcholu
        # Nezapomeň zkontrolovat, jestli není prázdný!
        else:
            return self.list.pop()
    
    def peek(self):
        if(self.isEmpty()):
            return  None
        
        else:# Podívá se na vrchol, ale neodebere
            return self.list[len(self.list) - 1]
    
zasobnik = Stack()
print(zasobnik.isEmpty())
zasobnik.push(1)
zasobnik.push(68)

print(zasobnik.peek())
print(zasobnik.isEmpty())
print(zasobnik.pop())
print(zasobnik.peek())
print(zasobnik.pop())
print(zasobnik.peek())
